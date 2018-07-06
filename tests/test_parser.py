#! /usr/bin/env python3
# coding: utf-8

from app.utils.parser import Parser


class TestParser:

    # Commented tests as they became unuseful after public methods changed into private ones.

    # def test_cut_into_sentences(self):
    #     sentences = self.parser._cut_into_sentences("Salut GrandPy ! Est-ce que tu connais, par hasard, l'adresse du centre équestre Cantegril ?")
    #     assert sentences == ["Salut GrandPy ", " Est-ce que tu connais", " par hasard", " l'adresse du centre équestre Cantegril ?"]

    # def test_choose_sentence(self):
    #     chosen_sentence = self.parser._choose_sentence(["Salut GrandPy ", " Est-ce que tu connais", " par hasard", " l'adresse du centre équestre Cantegril ?"])
    #     assert chosen_sentence == "Est-ce que tu connais l'adresse du centre équestre Cantegril ? "

    # def test_filter_words(self):
    #     relevant_words = self.parser._filter_words(["Salut", "GrandPy", "Est-ce", "que", "tu", "connais", "l", "adresse", "du", "centre", "équestre", "Cantegril", "?"])
    #     assert relevant_words == ["centre", "équestre", "Cantegril"]

    def test_parse(self):
        parser = Parser("Salut GrandPy ! Est-ce que tu connais, par hasard, l'adresse du centre équestre Cantegril ?")
        assert parser.query_relevant_words == ["centre", "équestre", "Cantegril"]
