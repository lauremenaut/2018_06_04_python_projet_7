#! /usr/bin/env python3
# coding: utf-8

from app.utils.parser import Parser


class TestParser:
    parser = Parser("Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?")

    def test_cut_into_sentences(self):
        sentences = self.parser.cut_into_sentences("salut vieux robot, quelle est l'adresse du cinéma le plus proche ?")
        assert sentences == ["salut vieux robot", " quelle est l'adresse du cinéma le plus proche ?"]

    def test_choose_sentence(self):
        chosen_sentence = self.parser.choose_sentence(["salut vieux robot", "quelle est l'adresse du cinéma le plus proche ?"])
        assert chosen_sentence == " quelle est l'adresse du cinéma le plus proche ?"

    def test_cut_chosen_sentence(self):
        words = self.parser.cut_chosen_sentence("quelle est l'adresse du cinéma le plus proche ?")
        assert words == ['quelle', 'est', 'l', 'adresse', 'du', 'cinéma', 'le', 'plus', 'proche', '?']

    def test_filter_words(self):
        filtered_words = self.parser.filter_words(['quelle', 'est', 'l', 'adresse', 'du', 'cinéma', 'le', 'plus', 'proche', '?'])
        assert filtered_words == ["cinéma"]

    def test_parser(self):
        filtered_words = self.parser.parser("Salut vieux robot, quelle est l'adresse du cinéma le plus proche ?")
        assert filtered_words == ["cinéma"]
