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
        pass

    def get_user_query(self):
        user_query = input('Bonjour mon petit, quelle est la question ?')
        # user_query = 'Quelle est l\'adresse de la piscine municipale ?'
        return user_query


def main():
    App()


if __name__ == '__main__':
    main()
