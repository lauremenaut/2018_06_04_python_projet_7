#! /usr/bin/env python3
# coding: utf-8

""" Set TestMediawikiApiRequest class."""

import app.utils.mediawiki_API_request as mediawiki


class TestMediawikiApiRequest:

    """ Set TestMediawikiApiRequest class.

    Consist of test_mediawiki_api_request() method.

    """

    def test_mediawiki_api_request(self, monkeypatch):
        """ Set test_mediawiki_api_request() method.

        Set a mock of MediaWikiApiRequest constructor.

        """

        class MockMediawiki:

            """ Set MockMediawiki class. """

            def __init__(self, lat, lng):
                """ MockMediawiki constructor.

                Set self.summary attribute.

                """
                self.summary = "Lorem ipsum"

        monkeypatch.setattr(mediawiki, 'MediaWikiApiRequest', MockMediawiki)

        mediawiki_api_request = mediawiki.MediaWikiApiRequest(
            42.9600983, 1.609331)

        assert mediawiki_api_request.summary == "Lorem ipsum"
