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

#     def test_choose_best_sentence_part(self):
#         chosen_part_of_query = self.parser._choose_best_sentence_part(
#             "Salut GrandPy ! Est-ce que tu connais, par hasard, \
# l'adresse du centre équestre Cantegril ?")
#         assert chosen_part_of_query == "Est-ce que tu connais \
# l'adresse du centre équestre Cantegril ? "

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
