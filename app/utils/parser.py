#! /usr/bin/env python3
# coding: utf-8

"""
Exemples de questions posées par l'utilisateur :
Salut GrandPy ! Est-ce que tu connais, par hasard, l'adresse d'OpenClassrooms ?
Bonjour GrandPy, comment ça va ? J'aimerais savoir comment aller au Jardin Botanique de Montréal.
J'aimerais aller voir la Tour Eiffel, peux-tu m'aider ?
Quelle est l'adresse de la piscine de Foix ?
Où se trouve l'Arc de triomphe à Paris ?
Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?
Comment aller à l'hôpital quand on habite à Laval ?
"""

import logging
import re

from app.utils.stop_words import stop_words
from app.utils.question_words import question_words
# from stop_words import stop_words
# from question_words import question_words

logging.basicConfig(filename="log.log", level=logging.DEBUG, format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')


class Parser:
    """ Sets App class.

    Consists of x (private) methods :
        - __init__()
        -
    """

    def __init__(self, user_query):
        """ App constructor.

        Manages ...

        """
        self.query = self.parser(user_query)

    def parser(self, user_query):
        try:
            sentences = self.cut_into_sentences(user_query)
            chosen_sentence = self.choose_sentence(sentences)
            words = self.cut_chosen_sentence(chosen_sentence)
            filtered_words = self.filter_words(words)
            # logging.debug("{} : Here are relevant words selected by parser : {}".format(filtered_words))

            # if filtered_words == []:
            #     raise Warning("Parser didn't find any relevant word ...")
            return filtered_words
        except:
            pass
        # except Warning as e:
        #     print("Error : '{}'".format(e))

    def cut_into_sentences(self, user_query):
        cut_sentences = re.split('[!,:;.]', user_query.lower())
        return cut_sentences

    def choose_sentence(self, sentences):
#  On fait une liste des phrases contenant au moins un mot contenu dans le fichier question_words.
        chosen_sentence = []
        for sentence in sentences:

#  On découpe chaque phrase en mots:
            words_of_sentence = self.cut_chosen_sentence(sentence)

#  Si un mot de la phrase est contenu dans le fichier question_words, alors la phrase est retenue
            for word in words_of_sentence:
                if word in question_words:
                    chosen_sentence.append(sentence)
                    break

#  Si aucune phrase ne contient de mot contenu dans le fichier question_words, alors, on garde toutes les phrases.
        if chosen_sentence == []:
            for sentence in sentences:
                chosen_sentence.append(sentence)

        returned_sentence = ""
        for sentence in chosen_sentence:
            returned_sentence += " " + sentence

        return returned_sentence

    def cut_chosen_sentence(self, chosen_sentence):
        split_words = []
#  On découpe la phrase en mots (à chaque espace)
        words = chosen_sentence.split()
#  On découpe les "mots" qui sont en fait des groupes de mots contenant une apostrophe
        for word in words:
            apostrophe_split = word.split("'")
            for apostrophe_word in apostrophe_split:
                split_words.append(apostrophe_word)
        return split_words

    def filter_words(self, words):
#  On fait une liste des mots qui ne sont pas contenus dans le fichier stop_words
        filtered_words = []
        for word in words:
            if word not in stop_words:
                filtered_words.append(word)
        return filtered_words


def main():
    parser = Parser("Où se trouve la tour Eiffel ?")
    print(parser.query)

if __name__ == '__main__':
    main()
