#! /usr/bin/env python3
# coding: utf-8

import requests

import app.utils.mediawiki_API_request as mediawiki


class TestMediawikiApiRequest:
    mediawiki_API_request = mediawiki.MediaWikiApiRequest(42.9600983, 1.609331)

    def test_get_pageid(self, monkeypatch):
        results = 898403

        # -tc- reprendre le mock comme dans test_gmaps_API_request.py.
        # mockreturn doit prendre deux paramètres et retourner une instance
        # d'une classe qui implémente une méthode json.
        def mockreturn(request):
            return results

        monkeypatch.setattr(mediawiki, 'get', mockreturn)
        assert self.mediawiki_API_request.get_pageid(42.9600983, 1.609331) == results



    def test_get_summary(self, monkeypatch):
        results = "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."

        def mockreturn(request):
            return results

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.mediawiki_API_request.get_summary(898403) == results



# class TestGmapsApiRequest:
#     gmaps_API_request = GmapsApiRequest()

#     def test_(self):
#         pass

"""
{'batchcomplete': '',
 'query':
    {'pages':
        {'898403':
            {'pageid': 898403,
             'ns': 0,
             'title': 'Festival de films Résistances',
             'extract': "Le Festival international de films Résistances, appelé plus simplement le Festival Résistances, se déroule à Foix en Ariège (Midi-Pyrénées) début juillet et propose une programmation de plus de 100 films, allant du documentaire à la fiction. Il est un des événements culturels les plus importants de la région.\nFondé en 1997, le festival s'inscrit dans un esprit de résistance à l'image des terres sur lesquels il a grandi. Il s'est donné comme objectif de promouvoir un cinéma engagé, rarement diffusé, et proposer un nouveau regard sur le monde.\nLe festival est peu à peu devenu l'un des événements majeurs de la contre-culture cinématographique en France."
             }
         }
     }
 }

"""
