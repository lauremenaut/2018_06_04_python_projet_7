#! /usr/bin/env python3
# coding: utf-8

""" Set TestGmapsApiRequest class. """

import app.utils.gmaps_API_request as gmaps


class TestGmapsApiRequest:

    """ Set TestGmapsApiRequest class.

    Consist of test_gmaps_api_request() method.

    """

    def test_gmaps_api_request(self, monkeypatch):
        """ Set test_gmaps_api_request() method.

        Set a mock of 'get' method from gmaps_api_request.py.

        """
        results = {
            "results": [
                {
                    'formatted_address': '1B Avenue du Général de Gaulle, \
09000 Foix, France',
                    'geometry': {
                        'location': {
                            'lat': 42.9600983,
                            'lng': 1.609331
                        }
                    }
                }
            ]
        }

        class MockResponse:

            """ Set MockResponse class.

            Consist of json() & status_code() methods.

            """

            def json(self):
                """ Set json() method. """
                return results

            def status_code(self):
                """ Set status_code() method. """
                return 200

        def mockreturn(url, params):
            """ Set mockreturn() method. """
            return MockResponse()

        monkeypatch.setattr(gmaps, 'get', mockreturn)

        gmaps_api_request = gmaps.GmapsApiRequest('piscine Foix')

        assert gmaps_api_request.address == (
            results["results"][0]['formatted_address'])
        assert gmaps_api_request.lat == (
            results["results"][0]['geometry']['location']['lat'])
        assert gmaps_api_request.lng == (
            results["results"][0]['geometry']['location']['lng'])
