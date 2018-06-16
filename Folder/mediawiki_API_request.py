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

    def __init__(self):
        """ MediaWikiApiRequest constructor.

        xxx

        """
        pass

    def get_article_title(self, lat_lng):
        """ Returns .

        xxx

        """

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
        title = data['query']['geosearch'][0]['title']
        return title


    def get_summary(self, title):
        """ Returns .

        xxx

        """

        parameters = {
            'action': 'query',
            'format': 'json'
            }

        response = get('https://fr.wikipedia.org/w/api.php',
                       params=parameters)
        data = response.json()
        summary = data['query']  # A compléter !
        return summary


def main():
    mediawiki_api_request = MediaWikiApiRequest()
    title = mediawiki_api_request.get_article_title("42.9600983|1.609331")
    print("Titre du 1er article : ", title)



if __name__ == '__main__':
    main()
