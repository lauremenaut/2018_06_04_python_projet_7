#! /usr/bin/env python3
# coding: utf-8

""" Set TestLocate class. """

import app.locate
from app.utils.messages import (ADDRESS_SUCCESS_MESSAGES,
                                PARSER_FAILURE_MESSAGES,
                                ADDRESS_FAILURE_MESSAGES,
                                SUMMARY_SUCCESS_MESSAGES,
                                SUMMARY_FAILURE_MESSAGES,
                                NEXT_QUESTION_MESSAGES)
from app.exceptions import GmapsApiError, MediaWikiApiError


class TestLocate:

    """ Set TestLocate class. """

    def test_locate_success(self, monkeypatch):
        """ Set test_locate_success() method. """
        class MockApis:

            """ Set MockApis class. """

            def __init__(self, param1="", param2=""):
                self.address = '1B Avenue du Général de Gaulle, 09000 Foix,\
 France'
                self.lat = 42.9600983
                self.lng = 1.609331
                self.summary = "Lorem ipsum"
        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Bonjour GrandPy, comment ça va ? \
J'aimerais savoir comment aller à la piscine de Foix.")

        assert locate_return[0] is False
        assert locate_return[1] in ADDRESS_SUCCESS_MESSAGES
        assert locate_return[2] == "1B Avenue du Général de Gaulle, 09000 \
Foix, France"
        assert locate_return[3] == 42.9600983
        assert locate_return[4] == 1.609331
        assert locate_return[5] in SUMMARY_SUCCESS_MESSAGES
        assert locate_return[6] == "Lorem ipsum"
        assert locate_return[7] in NEXT_QUESTION_MESSAGES

    def test_locate_parser_failure(self, monkeypatch):
        """ Set test_locate_parser_failure() method. """
        class MockApis:

            """ Set MockApis class. """

            def __init__(self, param1="", param2=""):
                pass

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Je ne sais pas ce que je cherche !")

        assert locate_return[0] is True
        assert locate_return[1] in PARSER_FAILURE_MESSAGES
        assert locate_return[2] is None
        assert locate_return[3] is None
        assert locate_return[4] is None
        assert locate_return[5] is None
        assert locate_return[6] is None
        assert locate_return[7] is None

    def test_locate_address_failure(self, monkeypatch):
        """ Set test_locate_address_failure() method. """
        class MockApis:

            """ Set MockApis class. """

            def __init__(self, param1="", param2=""):
                raise GmapsApiError()

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Je cherche l'adresse \
d'Openclassrooms")

        assert locate_return[0] is True
        assert locate_return[1] in ADDRESS_FAILURE_MESSAGES
        assert locate_return[2] is None
        assert locate_return[3] is None
        assert locate_return[4] is None
        assert locate_return[5] is None
        assert locate_return[6] is None
        assert locate_return[7] is None

    def test_locate_summary_failure(self, monkeypatch):
        """ Set test_locate_summary_failure() method. """
        class MockApis:

            """ Set MockApis class. """

            def __init__(self, param1="", param2=""):
                self.address = "Atlantic Ocean"
                self.lat = -14.5994134
                self.lng = -28.6731465
                if param2:
                    raise MediaWikiApiError()

        monkeypatch.setattr(app.locate, 'GmapsApiRequest', MockApis)
        monkeypatch.setattr(app.locate, 'MediaWikiApiRequest', MockApis)

        locate_return = app.locate.locate("Connais-tu l'Océan Atlantique ?")

        assert locate_return[0] is False
        assert locate_return[1] in ADDRESS_SUCCESS_MESSAGES
        assert locate_return[2] == "Atlantic Ocean"
        assert locate_return[3] == -14.5994134
        assert locate_return[4] == -28.6731465
        assert locate_return[5] in SUMMARY_FAILURE_MESSAGES
        assert locate_return[6] is None
        assert locate_return[7] in NEXT_QUESTION_MESSAGES
