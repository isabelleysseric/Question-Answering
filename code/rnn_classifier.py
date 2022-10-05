##
## ift7022-4022
## File description:
## rnn_classifier
##

import spacy
import numpy as np
import keras
from numpy import argmax
from keras import Sequential
from keras.layers import LSTM, Dense, Embedding, Bidirectional, SpatialDropout1D
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split


# Variables et constantes
path = "data/questions-train.txt"
MAX_LEN = 40
NB_CLASSE = 4


class Data:

    def __init__(self, path):
        self.raw_data = self.load_data(path)

    def load_data(self, path):
        with open(path, 'r') as fp:
            data = fp.readlines()
        return data
    
    def make_dummys(self, label):
        target =  { 'P' : 1,  # Person
                    'L' : 0,  # Location
                    'O' : 1,  # Organization
                    'T' : 2,  # Time Point
                    'R' : 2,  # Duration
                    'M' : 2,  # Money
                    'C' : 2,  # Percentage
                    'A' : 2,  # Amont
                    'D' : 2,  # Distance
                    'F' : 3,  # Description
                    'W' : 1,  # Title
                    'B' : 3,  # Definition
                    'Y' : 2,  # Age
                    'X' : 3   # Other
                  }
        result = np.zeros(NB_CLASSE)
        result[target[label]] = 1
        return np.asarray(result).astype(np.float32)

    def get_data(self):
      y = []
      x = []
      for line in self.raw_data:
        y.append(self.make_dummys(line[0]))
        x.append(line[2:])
      return train_test_split(x, y, test_size=0.2, random_state=42)


class Tokenise:

    def __init__(self, dataset, target, word2id, nlp_model):
        self.tokenized_dataset = [None for _ in range(len(dataset))]
        self.dataset = dataset
        self.target = target
        self.word2id = word2id
        self.nlp_model = nlp_model
        self.tokenize_dataset()

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        if self.tokenized_dataset[index] is None:
            self.tokenized_dataset[index] = self.tokenize(self.dataset[index])
            self.target[index] = self.target[index]
        return self.tokenized_dataset[index], self.target[index]

    def tokenize_dataset(self):
        for i in range(self.__len__()):
            self.__getitem__(i)

    def tokenize(self, sentence):
        return pad_sequences([[self.word2id.get(word.text, 1) for word in self.nlp_model(sentence)]], maxlen=MAX_LEN, padding='post')[0]


# Load the data
dataset = Data(path)
X_train, X_test, y_train, y_test = dataset.get_data()

nlp = spacy.load('en_core_web_lg')
embedding_size = nlp.meta['vectors']['width']
hidden_size = 100

word2id = {}
id2embedding = {}
id2word = {}

# Create ambbeding
word2id[1] = "<unk>"
id2embedding[1] = np.zeros(embedding_size, dtype=np.float64)
word_index = 2

for question in X_train:
    for word in nlp(question):
        if word.text not in word2id.keys():
            word2id[word.text] = word_index
            id2embedding[word_index] = word.vector
            id2word[word_index] = word.text
            word_index += 1

tokenizer_embbeding =  Tokenise([], [], word2id, nlp)



if __name__ == '__main__':
    
    # Start the training
    train_dataset = Tokenise(X_train, y_train, word2id, nlp)
    valid_dataset = Tokenise(X_test, y_test, word2id, nlp)

    # Create the model
    model = Sequential()
    model.add(Embedding(len(word2id) + 1, output_dim=64, input_length=MAX_LEN))
    model.add(SpatialDropout1D(0.2))
    model.add(Bidirectional(LSTM(128, recurrent_dropout=0.2)))
    model.add(Dense(NB_CLASSE, activation="softmax"))
    # display the model
    print(model.summary())
    model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=["accuracy"])

    x_train = np.array(train_dataset.tokenized_dataset)
    y_train = np.array(train_dataset.target)
    x_valide = np.array(valid_dataset.tokenized_dataset)
    y_valide = np.array(valid_dataset.target)

    # launch training phase
    print(x_train.shape,y_train.shape)
    print(x_valide.shape,y_valide.shape)
    model.fit(x_train, y_train, batch_size=32, epochs=15, validation_data=(x_valide, y_valide))
    model.save('model')

    # load the model and evaluate it
    new_model = keras.models.load_model('model')
    sentence = tokenizer_embbeding.tokenize("How long is the road from new york to paris ?")
    sentence = (np.array([sentence]))
    score = new_model.predict(sentence)
    print(argmax(score[0]))