#! /usr/bin/env python3
# coding: utf-8

""" Sets MediaWikiApiRequest class.

MediaWikiApiRequest class retrieves data from MediaWiki API.

"""

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
        self.summary = self.get_summary(pageid)

    def get_pageid(self, lat, lng):
        """ Returns .

        xxx

        """
        lat_lng = "|".join([str(lat), str(lng)])

        parameters = {
            'action': 'query',
            'list': 'geosearch',
            'gsradius': 5000,
            'gscoord': lat_lng,
            'format': 'json'
            }

        response = get('https://fr.wikipedia.org/w/api.php',
                       params=parameters)
        data = response.json()
        pageid = data['query']['geosearch'][0]['pageid']
        return pageid


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
