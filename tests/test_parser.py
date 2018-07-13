#! /usr/bin/env python3
# coding: utf-8

""" Set TestParser class. """

from app.utils.parser import Parser


class TestParser:

    """ Set TestParser class. """

    def test_parser(self):
        """ Set test_parser() method. """
        parser = Parser("Salut GrandPy ! Est-ce que tu connais, par hasard, \
l'adresse du centre équestre Cantegril ?")
        assert parser.query_relevant_words == [
            "centre", "équestre", "Cantegril"]

    # Commented tests as they became unuseful after public methods
    # changed into private ones.

#     parser = Parser("Salut GrandPy ! Est-ce que tu connais, par \
# hasard, l'adresse du centre équestre Cantegril ?")

#     def test_cut_into_sentences(self):
#         sentences = self.parser._cut_into_sentences("Salut GrandPy ! \
# Est-ce que tu connais, par hasard, l'adresse du centre équestre \
# Cantegril ?")
#         assert sentences == ["Salut GrandPy ", " Est-ce que tu \
# connais", " par hasard", " l'adresse du centre équestre Cantegril ?"]

#     def test_choose_sentence(self):
#         chosen_sentence = self.parser._choose_sentence(["Salut \
# GrandPy ", " Est-ce que tu connais", " par hasard", " l'adresse du \
# centre équestre Cantegril ?"])
#         assert chosen_sentence == "Est-ce que tu connais l'adresse \
# du centre équestre Cantegril ? "

#     def test_filter_words(self):
#         relevant_words = self.parser._filter_words(["Salut", "GrandPy\
# ", "Est-ce", "que", "tu", "connais", "l", "adresse", "du", "centre\
# ", "équestre", "Cantegril", "?"])
#         assert relevant_words == ["centre", "équestre", "Cantegril"]

#     def test_parse(self):
#         relevant_words = self.parser._parse("Salut GrandPy ! Est-ce \
# que tu connais, par hasard, l'adresse du centre équestre Cantegril \
# ?")
#         assert relevant_words == ["centre", "équestre", "Cantegril"]
