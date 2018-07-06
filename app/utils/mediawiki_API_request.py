#! /usr/bin/env python3
# coding: utf-8

""" Set MediaWikiApiRequest class.

MediaWikiApiRequest class retrieves data from MediaWiki API.

"""

import logging

from requests import get


class MediaWikiApiRequest:

    """ Set MediaWikiApiRequest class.

    Consist of 3 private methods :
        - __init__()
        - _get_page_id()
        - _get_summary()

    """

    def __init__(self, lat, lng):
        """ MediaWikiApiRequest constructor.

        Receive 2 floating numbers representing latitude & longitude.
        Set self.summary attribute.

        """
        pageid = self._get_pageid(lat, lng)
        if pageid:
            self.summary = self._get_summary(pageid)

    def _get_pageid(self, lat, lng):
        """ Set _get_pageid() method.

        Receive 2 floating numbers from contructor.
        Send request to MediaWiki API.
        Return an integer corresponding to the page ID of the MediaWiki article referenced as being next to the searched position.

        """
        lat_lng = "|".join([str(lat), str(lng)])

        parameters = {
            'action': 'query',
            'list': 'geosearch',
            'gsradius': 10000,
            'gscoord': lat_lng,
            'format': 'json'
            }

        response = get('https://fr.wikipedia.org/w/api.php',
                       params=parameters)
        # if response.status_code != 200:
        #     print("Erreur {} : problème d'accès à l'API MediaWiki".format(response.status_code))

        data = response.json()

        try:
            pageid = data['query']['geosearch'][0]['pageid']
            return pageid
        except KeyError as e:
            logging.warning(" MediaWiki didn't find any matching article ... KeyError : {}".format(e))
        except IndexError as e:
            logging.warning(" MediaWiki didn't find any matching article ... IndexError : {}".format(e))

    def _get_summary(self, pageid):
        """ Set _get_summary() method.

        Receive an integer representing page ID of MediaWiki.
        Send request to MediaWiki API.
        Return a string containing summary of MediaWiki article corresponding to page ID.

        """

        parameters = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'exintro': '',
            'explaintext': '',
            'pageids': pageid
            }

        response = get('https://fr.wikipedia.org/w/api.php',
                       params=parameters)
        data = response.json()
        summary = data['query']['pages'][str(pageid)]['extract']
        return summary
