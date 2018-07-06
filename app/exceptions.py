#! /usr/bin/env python3
# coding: utf-8

""" Set customised exceptions """


class ParserError(Exception):
    pass


class ApiError(Exception):
    pass


class GmapsApiError(ApiError):
    pass


class MediaWikiApiError(ApiError):
    pass
