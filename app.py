#! /usr/bin/env python3
# coding: utf-8


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
        self.user_query = self.get_user_query()
        self.words = self.cut_user_query(self.user_query)
        print(self.words)

    def get_user_query(self):
        # Sécuriser la saisie avec un try/except ??
        # user_query = input('Bonjour mon petit, quelle est ta question ?\n')
        user_query = 'Quelle est l\'adresse de la piscine municipale ?'
        return user_query

    def cut_user_query(self, user_query):
        words = user_query.split()
        return words


def main():
    App()


if __name__ == '__main__':
    main()
