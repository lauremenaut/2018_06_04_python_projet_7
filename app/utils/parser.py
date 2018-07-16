#! /usr/bin/env python3
# coding: utf-8

""" Set Parser class.

Parser class allows extracting relevant words from query submitted by
user.

"""

import re

from app.utils.question_words import QUESTION_WORDS
from app.utils.stop_words import STOP_WORDS


class Parser:

    """ Set Parser class.

    Consist of a constructor setting a public attribute containing
    a list of relevant words extracted from user query.

    """

    def __init__(self, user_query):
        """ Set Parser constructor.

        Receive a string containing user query.
        Set 'self.query_relevant_words' attribute calling _parse()
        method.

        """
        self.query_relevant_words = self._parse(user_query)

    def _parse(self, user_query):
        """ Set _parse() private method.

        Receive the string containing user query from constructor.
        Return a list of relevant words.

        """
        chosen_part_of_query = self._choose_best_sentence_part(user_query)
        words = re.split("[ ']", chosen_part_of_query)
        relevant_words = self._filter_words(words)
        return relevant_words

    def _choose_best_sentence_part(self, user_query):
        """ Set _choose_best_sentence_part() private method.

        Receive the string containing user query.
        Return a string containing choosen sentence part according to
        'question_words' list.

        """
        # Cut user query into different parts according punctuation,
        # except '?'.
        parts_of_query = re.split('[!,:;.]', user_query)

        chosen_part_of_query = []
        for part in parts_of_query:
            # Each part is cut into a list of words
            words = re.split("[ ']", part)
            # If at least one word is contained in question_words list,
            # then the part is added to 'chosen_part_of_query' list
            for word in words:
                if word in QUESTION_WORDS:
                    chosen_part_of_query.append(part.strip())
                    break
        # If no part was previously added to 'chosen_part_of_query',
        # then all parts are selected
        if chosen_part_of_query == []:
            for part in parts_of_query:
                chosen_part_of_query.append(part.strip())
        # All parts are concatenated into one string
        returned_part = ""
        for part in chosen_part_of_query:
            returned_part += part + " "
        return returned_part

    def _filter_words(self, words):
        """ Set _filter_words() private method.

        Reveive a list of words.
        Return a list of relevant words.

        """
        relevant_words = []
        # Words that don't appear in 'stop_words' list are added to
        # 'relevant_words' list
        for word in words:
            if word.lower() not in STOP_WORDS:
                relevant_words.append(word)
        return relevant_words
