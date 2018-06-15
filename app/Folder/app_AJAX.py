#! /usr/bin/env python3
# coding: utf-8

"""
Exemples de questions posées par l'utilisateur :
Salut GrandPy ! Est-ce que tu connais, par hasard, l'adresse d'OpenClassrooms ?
Où se trouve l'Arc de triomphe à Paris ?
Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?
Bonjour GrandPy, comment ça va ? J'aimerais savoir comment aller au Pharmaprix d'Ahuntsic.
Quelle est l'adresse de la piscine de Foix ?
Comment aller à l'hôpital quand on habite à Laval ?
J'aimerais aller voir la Tour Eiffel, peux-tu m'aider ?
"""

import re

from gmaps_API_request import GmapsApiRequest
from mediawiki_wrapper import MediaWikiWrapper

from stop_words import stop_words
from question_words import question_words


class App:
    """ Sets App class.

    Consists of x (private) methods :
        - __init__()
        -
    """

    def __init__(self, user_query):
        """ App constructor.

        Manages ...

        """
        self.run(user_query)

    def run(self, user_query):
        carry_on = True
        while carry_on:
            try:
                query = self.parser(user_query)
            except IndexError:
                print("\nDis-moi ça plus clairement s'il te plait !")
                continue
            try:
                gmaps_api_request = GmapsApiRequest(query)
                address = gmaps_api_request.address
                lat = gmaps_api_request.lat
                lng = gmaps_api_request.lng
                print("\nOh oui, je connais ! Tu trouveras ça au", address)
            except IndexError:
                print("\nÇa, je ne m'en souviens plus ...")
                continue
            try:
                mediawiki_wrapper = MediaWikiWrapper(lat, lng)
                summary = mediawiki_wrapper.summary
                print("\nEn parlant de ça, j'avais une petite chose à te raconter ! ")
                print(summary)
            except:  # Je ne connais pas le type d'erreur levée ...
                print("\nEtrangement, je ne connais aucune anecdote à ce sujet !")

    def parser(self, user_query):
        query = self.lower_user_query(user_query)
        sentences = self.cut_into_sentences(query)
        chosen_sentence = self.choose_sentence(sentences)
        words = self.cut_chosen_sentence(chosen_sentence)
        filtered_words = self.filter_words(words)
        return filtered_words

    def lower_user_query(self, user_query):
        user_query_lower = user_query.lower(user_query)
        return user_query_lower

    def cut_into_sentences(self, user_query):
        cut_sentences = re.split('[!,:;.]', user_query)
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
    app = App()
    app.run()

if __name__ == '__main__':
    main()
