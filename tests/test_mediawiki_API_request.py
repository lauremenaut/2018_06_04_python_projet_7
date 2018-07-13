#! /usr/bin/env python3
# coding: utf-8

""" Set TestMediawikiApiRequest class.

TestMediawikiApiRequest class set a mock of 'get' method from mediawiki_API_request.py.

"""

import app.utils.mediawiki_API_request as mediawiki


class TestMediawikiApiRequest:
    """ Set TestMediawikiApiRequest class. """

    def test_mediawiki_api_request(self, monkeypatch):
        """ Set test_get_pageid() method. """

        class MockMediawiki:
            """ Set MockResponse class. """
            def __init__(self, lat, lng):
                self.summary = "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."

        monkeypatch.setattr(mediawiki, 'MediaWikiApiRequest', MockMediawiki)

        mediawiki_API_request = mediawiki.MediaWikiApiRequest(42.9600983, 1.609331)

        assert mediawiki_API_request.summary == "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."
