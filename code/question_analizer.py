
import numpy as np
import keras
import spacy
from rnn_classifier import tokenizer_embbeding
from enum import Enum
import re


# Variables
nlp = spacy.load("en_core_web_lg")
regexpr = {
    "who"   : r"^[Ww]ho",
    "where" : r"^[Ww]here",
    "when"  : r"^[Ww]hen"
}


class QuestionType(Enum):
    L = 0   # Location
    H = 1   # Human
    N = 2   # Numeric
    E = 3   # Entity


class Question:

    def __init__(self):
        self.tokenizer = tokenizer_embbeding
        self.model = keras.models.load_model('model')

    def fit(self, question):
        self.keyword = []
        self.question = question
        self.determine_QT()
        self.find_keyword()
        
    def determine_QT_withregexpr(self):
        # check with reg expr for simple question
        if re.search(regexpr['who'], self.question):
            self.qt = QuestionType.H
            return True
        if re.search(regexpr['where'], self.question):
            self.qt = QuestionType.L
            return True
        if re.search(regexpr['when'], self.question):
            self.qt = QuestionType.N
            return True
        return False

    def determine_QT(self):
        if not self.determine_QT_withregexpr():
            # check with rnn for more complex question
            sentence = self.tokenizer.tokenize(self.question)
            sentence = (np.array([sentence]))
            score = self.model.predict(sentence)
            self.qt = QuestionType(np.argmax(score[0]))

    def find_keyword(self):
        words_question = ['why', 'who', 'when', 'where', 'What', 'how']
        word_list = nlp(self.question)
        for word in word_list:
            if not word.text.lower() in words_question and not word.is_punct and \
                    not word.is_stop and not word.dep_ == 'aux' and \
                    not word.dep_ == 'det':
                self.keyword.append(word.text)
        return self.keyword
