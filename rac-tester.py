#!/usr/bin/env python3
import csv
import codecs
import colorama
from colorama import Fore, Style
import sys
import random

class Question:
    def __init__(self, qid, q_fr, r_fr_correct, r_fr_wrong1, r_fr_wrong2, r_fr_wrong3,
                            q_en, r_en_correct, r_en_wrong1, r_en_wrong2, r_en_wrong3):
        self.qid=qid
        self.q_fr=q_fr
        self.r_fr_list= [ ]
        self.r_fr_list.append(r_fr_correct)
        self.r_fr_list.append(r_fr_wrong1)
        self.r_fr_list.append(r_fr_wrong2)
        self.r_fr_list.append(r_fr_wrong3)
        self.r_fr_correct=r_fr_correct
        self.q_en=q_en
        self.r_en_list= [ ]
        self.r_en_list.append(r_en_correct)
        self.r_en_list.append(r_en_wrong1)
        self.r_en_list.append(r_en_wrong2)
        self.r_en_list.append(r_en_wrong3)
        self.r_en_correct=r_en_correct

    def __str__(self):
        return "question {}".format(self.qid)
    def __repr__(self):
        return self.__str__() 

    def AskMeFrench(self):
        print('{}'.format(self.q_fr))

        random.shuffle(self.r_fr_list)
        for idx, answer in enumerate(self.r_fr_list):
            print('\t{}: {}'.format(idx, answer))

        pick = input('Réponse? ')
        pick = int(pick)

        if(self.r_fr_correct in self.r_fr_list[pick]):
            print(Fore.GREEN+'Bonne réponse!'+Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + 'Mauvais réponse. La bonne réponse est: {}'.format(self.r_fr_correct) + Style.RESET_ALL)
            return False

    def AskMeEnglish(self):
        print('{}'.format(self.q_en))
        random.shuffle(self.r_en_list)
        for idx, answer in enumerate(self.r_en_list):
            print('\t{}: {}'.format(idx, answer))
        pick = input('Answer? ')
        pick = int(pick)

        if(self.r_en_correct in self.r_en_list[pick]):
            print(Fore.GREEN+'Right Answer!'+Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + 'Wrong Answer. The correct answer is: {}'.format(self.r_en_correct) + Style.RESET_ALL )
            return False

    def AskMe(self, lang):
        if 'fr' in lang:
            return self.AskMeFrench()
        else:
            return self.AskMeEnglish()




nb_questions=10
language='fr'
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Erreur: ficher CSV de question nécessaire")
        print("Usage: {} <Nombre de question> [fr,en]".format(sys.argv[0]))
        print("Error: CSV question file needed")
        print("Usage: {} <Number of question> [en,fr]".format(sys.argv[0]))
        exit()
    if len(sys.argv) >= 3:
        nb_questions = int(sys.argv[2])
    if len(sys.argv) >= 4:
        if 'fr' in sys.argv :
            language='fr'
        elif 'en' in sys.argv :
            language='en'

    questions_list = []
    wrong_answer = 0
    right_answer = 0
    with codecs.open(sys.argv[1], 'r','ISO-8859-1') as csvfile:
       qReader  = csv.reader( csvfile, delimiter=';')
       next(qReader, None)
       for row in qReader:
           questions_list.append(Question(row[0],
                                          row[6],
                                          row[7],
                                          row[8],
                                          row[9],
                                          row[10],
                                          row[1],
                                          row[2],
                                          row[3],
                                          row[4],
                                          row[5]))

    for i in range(0, nb_questions):
        #q = questions_list[1]
        q = random.choice(questions_list)
        if q.AskMe(language):
            right_answer +=1
        else:
            wrong_answer +=1
    print()
    if 'fr' in language:
        print('Résumé')
        print('Réponses correctes: {}'.format(right_answer))
        print('Réponses incorrectes: {}'.format(wrong_answer))
        print('Ratio: {}'.format(right_answer/(float(nb_questions))))
    else:
        print('Summary')
        print('Right answers: {}'.format(right_answer))
        print('Wrong answers: {}'.format(wrong_answer))
        print('Ratio: {}'.format(right_answer/(float(nb_questions))))

