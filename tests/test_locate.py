#! /usr/bin/env python3
# coding: utf-8

from app.utils.messages import address_success_messages, parser_failure_messages, address_failure_messages, summary_success_messages, summary_failure_messages, next_question_messages
import app.locate


class TestLocate:

    def test_locate_success(self, monkeypatch):

        class MockApis:
            """ Set MockResponse class. """
            def __init__(self, param1="", param2=""):
                self.address = '1B Avenue du Général de Gaulle, 09000 Foix, France'
                self.lat = 42.9600983
                self.lng = 1.609331
                self.summary = "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Bonjour GrandPy, comment ça va ? J'aimerais savoir comment aller à la piscine de Foix.")

        assert locate_return[0] is False
        assert locate_return[1] in address_success_messages
        assert locate_return[2] == "1B Avenue du Général de Gaulle, 09000 Foix, France"
        assert locate_return[3] == 42.9600983
        assert locate_return[4] == 1.609331
        assert locate_return[5] in summary_success_messages
        assert locate_return[6] == "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."
        assert locate_return[7] in next_question_messages

    def test_locate_parser_failure(self, monkeypatch):

        class MockApis:
            """ Set MockResponse class. """
            def __init__(self, param1="", param2=""):
                self.address is None
                self.lat is None
                self.lng is None
                self.summary is None

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Je ne sais pas ce que je cherche !")

        assert locate_return[0] is True
        assert locate_return[1] in parser_failure_messages
        assert locate_return[2] is None
        assert locate_return[3] is None
        assert locate_return[4] is None
        assert locate_return[5] is None
        assert locate_return[6] is None
        assert locate_return[7] is None

    def test_locate_address_failure(self, monkeypatch):

        class MockApis:
            """ Set MockResponse class. """
            def __init__(self, param1="", param2=""):
                self.address is None
                self.lat is None
                self.lng is None
                self.summary is None

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Je cherche l'adresse d'Openclassrooms")

        assert locate_return[0] is True
        assert locate_return[1] in address_failure_messages
        assert locate_return[2] is None
        assert locate_return[3] is None
        assert locate_return[4] is None
        assert locate_return[5] is None
        assert locate_return[6] is None
        assert locate_return[7] is None

    def test_locate_summary_failure(self, monkeypatch):

        class MockApis:
            """ Set MockResponse class. """
            def __init__(self, param1="", param2=""):
                self.address = "Atlantic Ocean"
                self.lat = -14.5994134
                self.lng = -28.6731465
                self.summary is None

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Connais-tu l'Océan Atlantique ?")

        assert locate_return[0] is False
        assert locate_return[1] in address_success_messages
        assert locate_return[2] == "Atlantic Ocean"
        assert locate_return[3] == -14.5994134
        assert locate_return[4] == -28.6731465
        assert locate_return[5] in summary_failure_messages
        assert locate_return[6] is None
        assert locate_return[7] in next_question_messages
