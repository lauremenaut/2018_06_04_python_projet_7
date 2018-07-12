#! /usr/bin/env python3
# coding: utf-8

import app.utils.mediawiki_API_request as mediawiki


class TestMediawikiApiRequest:
    mediawiki_API_request = mediawiki.MediaWikiApiRequest(42.9600983, 1.609331)

    def test_get_pageid(self, monkeypatch):
        results = {
            "query": {
                "geosearch": [
                    {
                        "pageid": 898403
                    }
                ]
            }
        }

        class Mockresponse:
            def json(self):
                return results

        def mockreturn(url, params):
            return Mockresponse()

        monkeypatch.setattr(mediawiki, 'get', mockreturn)
        assert self.mediawiki_API_request._get_pageid(42.9600983, 1.609331) == results['query']['geosearch'][0]['pageid']

    def test_get_summary(self, monkeypatch):
        results = {
            'query': {
                'pages': {
                    '898403': {
                        'extract': "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."
                    }
                }
            }
        }

        class Mockresponse:
            def json(self):
                return results

        def mockreturn(url, params):
            return Mockresponse()

        monkeypatch.setattr(mediawiki, 'get', mockreturn)
        assert self.mediawiki_API_request._get_summary(898403) == results['query']['pages']['898403']['extract']
