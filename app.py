#! /usr/bin/env python3
# coding: utf-8

"""
Exemples de questions posées par l'utilisateur :
- Où se trouve l'Arc de triomphe à Paris ?
- Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?
- Bonjour GrandPy, comment ça va ? J'aimerais savoir comment aller à la FNAC de Toulouse.
- Quelle est l'adresse de la piscine de Foix ?
"""

import json

from gmaps_API_request import GmapsApiRequest
from mediawiki_wrapper import MediaWikiWrapper


class App:
    """ Sets App class.

    Consists of x (private) methods :
        - __init__()
        -
    """

    def __init__(self):
        """ App constructor.

        Manages ...

        """
        pass

    def run(self):
        carry_on = True
        while carry_on:
            try:
                query = self.parser()
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
                print("\nEn parlant de ça, savais-tu que ")
                print(summary)
            except:  # Je ne connais pas le type d'erreur levée ...
                pass

    def parser(self):
        user_query = self.get_user_query()
        print("\nUser query : ", user_query)
        sentences = self.cut_into_sentences(user_query)
        print("Sentences : ", sentences)
        chosen_sentence = self.choose_sentence(sentences)
        print("Chosen sentences : ", chosen_sentence)
        words = self.cut_chosen_sentence(chosen_sentence[-1])  # Au cas où il y ait plusieurs phrases sélectionnées, on choisit la dernière.
        print("Words : ", words)
        filtered_words = self.filter_words(words)
        print("Filtered words : ", filtered_words)
        return filtered_words

    def get_user_query(self):
        user_query = input('\nAs-tu une question pour moi mon petit ?\n\n')
        # user_query = "quelle est l'adresse du cinéma le plus proche ?"
        user_query_lower = user_query.lower()
        return user_query_lower

    def cut_into_sentences(self, user_query):
        # Ajouter aussi les autres signes de ponctuation :;?!.
        sentences = user_query.split(",")
        return sentences

    def choose_sentence(self, sentences):
        chosen_sentence = []
        for sentence in sentences:
        # Peut-on faire plus élégant ? Est-on obligé de vérifier "ou" et "où" ?
            if ("?" or "ou" or "où" or "comment" or "quel" or "quelle" or "est-ce" or "connais-tu" or "connaissez-vous") in sentence:
                chosen_sentence.append(sentence)
        if chosen_sentence == []:
            for sentence in sentences:
                chosen_sentence.append(sentence)
        return chosen_sentence

    def cut_chosen_sentence(self, chosen_sentence):
        words = chosen_sentence.split()
        return words

    def filter_words(self, words):
        with open("stop_words.json", 'r') as f:
            stop_words = json.load(f)

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
