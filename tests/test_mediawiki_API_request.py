#! /usr/bin/env python3
# coding: utf-8

import requests

from app.utils.mediawiki_API_request import MediaWikiApiRequest


class TestMediawikiApiRequest:
    mediawiki_API_request = MediaWikiApiRequest(42.9600983, 1.609331)

    def test_get_pageid(self, monkeypatch):
        results = 898403

        def mockreturn(request):
            return results

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.mediawiki_API_request._get_pageid(42.9600983, 1.609331) == results



    def test_get_summary(self, monkeypatch):
        results = "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."

        def mockreturn(request):
            return results

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.mediawiki_API_request._get_summary(898403) == results
