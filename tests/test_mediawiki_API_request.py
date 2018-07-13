#! /usr/bin/env python3
# coding: utf-8

""" Set TestMediawikiApiRequest class.

TestMediawikiApiRequest class set a mock of 'get' method from
mediawiki_API_request.py.

"""

import app.utils.mediawiki_api_request as mediawiki


class TestMediawikiApiRequest:

    """ Set TestMediawikiApiRequest class. """

    def test_mediawiki_api_request(self, monkeypatch):
        """ Set test_mediawiki_api_request() method. """

        class MockMediawiki:

            """ Set MockMediawiki class. """

            def __init__(self, lat, lng):
                self.summary = "Lorem ipsum"

        monkeypatch.setattr(mediawiki, 'MediaWikiApiRequest', MockMediawiki)

        mediawiki_api_request = mediawiki.MediaWikiApiRequest(
            42.9600983, 1.609331)

        assert mediawiki_api_request.summary == "Lorem ipsum"
