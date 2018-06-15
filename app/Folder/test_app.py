#! /usr/bin/env python3
# coding: utf-8

from appl import App
import builtins


class TestApp:
    app = App()

    def test_get_user_query(self, monkeypatch):

        def mock_input(arg):
            return "Où se trouve la Tour Eiffel ?"

        monkeypatch.setattr(builtins, "input", mock_input)

        user_query = self.app.get_user_query()
        assert user_query == "où se trouve la tour eiffel ?"

    def test_cut_into_sentences(self):
        sentences = self.app.cut_into_sentences("salut vieux robot, quelle est l'adresse du cinéma le plus proche ?")
        assert sentences == ["salut vieux robot", " quelle est l'adresse du cinéma le plus proche ?"]

    def test_choose_sentence(self):
        chosen_sentence = self.app.choose_sentence(["salut vieux robot", "quelle est l'adresse du cinéma le plus proche ?"])
        assert chosen_sentence[-1] == "quelle est l'adresse du cinéma le plus proche ?"

    def test_cut_chosen_sentence(self):
        words = self.app.cut_chosen_sentence("quelle est l'adresse du cinéma le plus proche ?")
        assert words == ['quelle', 'est', "l'adresse", 'du', 'cinéma', 'le', 'plus', 'proche', '?']

    def test_filter_words(self):
        filtered_words = self.app.filter_words(['quelle', 'est', "l'adresse", 'du', 'cinéma', 'le', 'plus', 'proche', '?'])
        assert filtered_words == ["cinéma"]
