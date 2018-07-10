#! /usr/bin/env python3
# coding: utf-8

""" Set Parser class.

Parser class allows extracting relevant words from query submitted by user.

"""

import re

from app.utils.stop_words import stop_words
from app.utils.question_words import question_words


class Parser:

    """ Set Parser class.

    Consist of 4 private methods :
        - _parse()
        - _cut_into_sentences()
        - _choose_sentence()
        - _filter_words()

    """

    def __init__(self, user_query):
        """ Parser constructor.

        Receive a string containing user query.
        Set 'self.query_relevant_words' attribute calling _parse() method.

        """
        self.query_relevant_words = self._parse(user_query)

    def _parse(self, user_query):
        """ Set _parse() method.

        Receive the string containing user query from constructor.
        Return a list of relevant words.

        """
        sentences = self._cut_into_sentences(user_query)
        chosen_sentence = self._choose_sentence(sentences)
        words = re.split("[ ']", chosen_sentence)
        relevant_words = self._filter_words(words)
        return relevant_words

    def _cut_into_sentences(self, user_query):
        """ Set _cut_into_sentences() method.

        Receive the string containing user query.
        Return a list containing sentences from user query cut according punctuation, except '?'.

        """
        cut_sentences = re.split('[!,:;.]', user_query)
        return cut_sentences

    def _choose_sentence(self, sentences):
        """ Set _choose_sentence() method.

        Receive a list of sentences.
        Return a string containing choosen sentence according 'question words'.

        """
        chosen_sentence = []
        for sentence in sentences:
            # Each sentence is cut into a list of words
            words_of_sentence = re.split("[ ']", sentence)
            # If at least one word is contained in 'question_words' list, then
            # the sentence is added to 'chosen_sentence' list
            for word in words_of_sentence:
                if word in question_words:  # or re.match(r"^[A-Z]", word[0]):  # Add comment for re.match if kept
                    chosen_sentence.append(sentence.strip())
                    break
        # If no sentence was previously added to 'chosen_sentence', then all sentences are selected
        if chosen_sentence == []:
            for sentence in sentences:
                chosen_sentence.append(sentence.strip())
        # All sentences are concatenated into one string
        returned_sentence = ""
        for sentence in chosen_sentence:
            returned_sentence += sentence + " "
        return returned_sentence

    def _filter_words(self, words):
        """ Set _filter_words() method.

        Reveive a list of words.
        Return a list of relevant words.

        """
        relevant_words = []
        # Words that don't appear in 'stop_words' list are added to 'relevant_words' list
        for word in words:
            if word.lower() not in stop_words:
                relevant_words.append(word)
        return relevant_words
