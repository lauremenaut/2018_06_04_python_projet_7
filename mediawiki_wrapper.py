#! /usr/bin/env python3
# coding: utf-8

""" Sets MediaWikiWrapper class.

MediaWikiWrapper class retrieves data from Wikipedia website with Python library "pymediawiki" as Mediawiki API wrapper.
https://github.com/barrust/mediawiki
pip install pymediawiki

"""

from mediawiki import MediaWiki


class MediaWikiWrapper:

    """ Sets MediaWikiWrapper class.

    Consists of xxx (private) methods :
        - __init__()
        - _get

    """

    def __init__(self, lat, lng):
        """ MediaWikiWrapper constructor.

        xxx

        """
        self.wikipedia = MediaWiki(lang=u'fr')
        self.title, self.summary = self.get_article(lat, lng)

    def get_article(self, lat, lng):
        """ Returns .

        xxx

        """
        article_title = self.wikipedia.geosearch(latitude=lat, longitude=lng)
        article_page = self.wikipedia.page(article_title[0])

        return article_title[0], article_page.summary

def main():
    mediawiki = MediaWikiWrapper(42.9600983, 1.609331)
    title = mediawiki.title
    print("\nTitre du 1er article : ", title)
    summary = mediawiki.summary
    print("\nRésumé : ", summary)

if __name__ == '__main__':
    main()
