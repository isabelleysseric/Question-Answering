##
## ift7022-4022
## File description:
## answer_system
##

from recherche_infos import ix, search_content
from termcolor import colored
from question_analizer import QuestionType
import spacy


# Variables
nlp = spacy.load("en_core_web_lg")
spacy_type_to_question_answer = {
    'PERSON' :      QuestionType.H,
    'NORP' :        QuestionType.L,
    'FAC' :         QuestionType.L,
    'ORG' :         QuestionType.H,
    'GPE' :         QuestionType.L,
    'LOC' :         QuestionType.L,
    'PRODUCT' :     QuestionType.E,
    'EVENT' :       QuestionType.E,
    'WORK_OF_ART' : QuestionType.H,
    'LAW' :         QuestionType.E,
    'LANGUAGE' :    QuestionType.E,
    'DATE' :        QuestionType.N,
    'TIME' :        QuestionType.N,
    'PERCENT' :     QuestionType.N,
    'MONEY' :       QuestionType.N,
    'QUANTITY' :    QuestionType.N,
    'ORDINAL' :     QuestionType.E,
    'CARDINAL' :    QuestionType.E
}


def is_type_match(sentence, question_type):
    # Check if a word match the question type
    word_list = nlp(sentence)
    for word in word_list.ents:
        if spacy_type_to_question_answer[word.label_] == question_type:
            return True
    return False

def define_best_answer(question, result, nb):
    respondes = []
    for elem in result:
        if is_type_match(elem[0], question.qt):
            respondes.append(elem)
        # if the number of document given by the user is respect
        if len(respondes) == nb:
            break
    # if no answer match the type
    if len(respondes) == 0:
        print(colored("No résultat find with answer type, there are document find only with keyword", "red"))
        respondes = result[0:min(len(result), nb)]
    return respondes

def get_answer(question, nb):
    result = search_content(' '.join(question.keyword), ix, nb)
    if len(result) == 0:
        return [(colored("NO ANSWER FOUND", 'red'), 'NOTHING')]
    result = define_best_answer(question, result, nb)    
    return result
