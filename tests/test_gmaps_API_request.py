#! /usr/bin/env python3
# coding: utf-8

import requests

from app.utils.gmaps_API_request import GmapsApiRequest


class TestGmapsApiRequest:

    gmaps_API_request = GmapsApiRequest('piscine Foix')

    def test_get_position_info(self, monkeypatch):
        results = {
            "results": [
                {
                    'address_components': {
                        'formatted_address': '1B Avenue du Général de Gaulle, 09000 Foix, France',
                        'geometry': {
                            'location': {
                                'lat': 42.9600983,
                                'lng': 1.609331
                            }
                        }
                    }
                }
            ]
        }

        class MockResponse:
            def json(self):
                return results

        def mockreturn(url, params):
            return MockResponse()

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.gmaps_API_request._get_position_info('piscine Foix') == results["results"][0]
