#! /usr/bin/env python3
# coding: utf-8

""" Set customised exceptions """


class ParserError(Exception):

    """ Set ParserError customised exception """

    pass


class GmapsApiError(Exception):

    """ Set GmapsApiError customised exception """

    pass


class MediaWikiApiError(Exception):

    """ Set MediaWikiApiError customised exception """

    pass
