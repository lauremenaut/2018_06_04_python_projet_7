#! /usr/bin/env python3
# coding: utf-8

"""
Exemples de questions posées par l'utilisateur :
- Où se trouve la Tour Eiffel ?
- Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?
- Bonjour GrandPy, comment vas-tu ? J'aimerais savoir comment aller à la FNAC de Toulouse.

"""

import json


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
        with open("stop_words.json", 'r') as f:
            self.stop_words = json.load(f)

    def parser(self):
        user_query = self.get_user_query()
        print("User query : ", user_query)
        sentences = self.cut_into_sentences(user_query)
        print("Sentences : ", sentences)
        chosen_sentence = self.choose_sentence(sentences)
        print("Chosen sentences : ", chosen_sentence)
        words = self.cut_chosen_sentence(chosen_sentence[-1])  # Au cas où il y ait plusieurs phrases sélectionnées, on choisit la dernière.
        print("Words : ", words)
        filtered_words = self.filter_words(words)
        print("Filtered words : ", filtered_words)

    def get_user_query(self):
        user_query = input('Bonjour mon petit, quelle est ta question ?\n')
        user_query_lower = user_query.lower()
        # user_query = 'Où se trouve la Tour Eiffel ?'
        return user_query_lower

    def cut_into_sentences(self, user_query):
        # Ajouter aussi les autres signes de ponctuation :;?!.
        sentences = user_query.split(",")
        return sentences

    def choose_sentence(self, sentences):
        chosen_sentence = []
        for sentence in sentences:
        # Ajouter aussi les mots-clés : ‘connais-tu’, ‘ou est’, ‘quel est’, adresse ...
            if "?" in sentence:
                chosen_sentence.append(sentence)
        return chosen_sentence

    def cut_chosen_sentence(self, chosen_sentence):
        words = chosen_sentence.split()
        return words

    def filter_words(self, words):
        filtered_words = []
        for word in words:
            if word not in self.stop_words:
                filtered_words.append(word)
        return filtered_words

def main():
    app = App()
    app.parser()


if __name__ == '__main__':
    main()
