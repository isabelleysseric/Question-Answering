

from termcolor import colored
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help="Number of documents return")
args = parser.parse_args()

print(colored("\nINITIALISATION\n", 'green'))

from answer_system import get_answer
from question_analizer import Question


def display_answer(result):
    for elem in result:
        if elem[1] == 'NOTHING':
            print(elem[0])
            break
        print(colored("Document ID:", "blue"), elem[1])
        print(elem[0])


question_str = ''
question = Question()
nb = 1
if args.n:
    nb = args.n
print(colored("\nSTARTING THE QA SYSTEM", 'green'))
question_str = input("\nEnter a question: ")
while question_str.lower() != "exit":
    if question_str == '':
        print(colored("Please enter a valide question\n", 'yellow'))
        question_str = input("Enter a question: ")
        continue
    question.fit(question_str)
    display_answer(get_answer(question, nb))
    question_str = input("\nEnter a question: ")
