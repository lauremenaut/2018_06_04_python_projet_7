#! /usr/bin/env python3
# coding: utf-8

""" Sets MediaWikiApiRequest class.

MediaWikiApiRequest class retrieves data from MediaWiki API.

"""
import logging

from requests import get


class MediaWikiApiRequest:

    """ Sets MediaWikiApiRequest class.

    Consists of xxx (private) methods :
        - __init__()
        - _get

    """

    def __init__(self, lat, lng):
        """ MediaWikiApiRequest constructor.

        xxx

        """
        pageid = self.get_pageid(lat, lng)
        print(lat, lng)
        if pageid:
            self.summary = self.get_summary(pageid)

    def get_pageid(self, lat, lng):
        """ Returns .

        xxx

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
        if response.status_code != 200:
            print("Erreur {} : problème d'accès à l'API MediaWiki".format(response.status_code))

        data = response.json()

        try:
            pageid = data['query']['geosearch'][0]['pageid']
            return pageid
        except KeyError as e:
            logging.warning(" MediaWiki didn't find any matching article ... KeyError : '{}'".format(e))
            return None
        except IndexError as e:
            logging.warning(" MediaWiki didn't find any matching article ... Error : '{}'".format(e))
            return None


    def get_summary(self, pageid):
        """ Returns .

        xxx

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


def main():
    mediawiki_api_request = MediaWikiApiRequest(42.9600983, 1.609331)
    summary = mediawiki_api_request.summary
    print("Résumé : ", summary)

if __name__ == '__main__':
    main()
