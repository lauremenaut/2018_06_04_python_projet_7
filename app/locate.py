#! /usr/bin/env python3
# coding: utf-8

""" Sets locate() function (called in query_locate() view function). """

import logging
import random

from app.exceptions import ParserError, GmapsApiError, MediaWikiApiError
from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import (ADDRESS_SUCCESS_MESSAGES,
                                PARSER_FAILURE_MESSAGES,
                                ADDRESS_FAILURE_MESSAGES,
                                SUMMARY_SUCCESS_MESSAGES,
                                SUMMARY_FAILURE_MESSAGES,
                                NEXT_QUESTION_MESSAGES)


def locate(query):
    """ Set locate() function.

    Receive a string containing user query.
    Use Parser, GmapsApiRequest and MediaWikiApiRequest classes.
    Return a list of 8 variables :
    - error : a boolean, False if an address is found, else True
    - message : a string randomly chosen in messages lists
    - address : a string containing the address of the searched place
    (sent back by Google Maps API), or None
    - lat : a floating number representing latitude (sent back by Google
    Maps API), or None
    - lng : a floating number representing longitude (sent back by
    Google Maps API), or None
    - summary_message : a string randomly chosen in messages lists, or
    None
    - summary : a string containing information about the searched place
    (sent back by MediaWiki API), or None
    - next_question_message : a string randomly chosen in messages
    list, or None

    """
    # 'error' variable is True only if no address is returned (parser
    # failure & address failure)
    def return_infos(error=False,
                     message=random.choice(ADDRESS_SUCCESS_MESSAGES),
                     address=None,
                     lat=None,
                     lng=None,
                     summary_message=random.choice(SUMMARY_SUCCESS_MESSAGES),
                     summary=None,
                     next_question_message=random.choice(
                         NEXT_QUESTION_MESSAGES)):
        """ Set return_infos() method. """
        if error:
            summary_message = None
            next_question_message = None

        return (error, message, address, lat, lng,
                summary_message, summary, next_question_message)

    try:
        parser = Parser(query)
        logging.debug("Here are relevant words selected by parser : %s",
                      parser.query_relevant_words)

        if not parser.query_relevant_words:
            raise ParserError("Parser didn't find any relevant word ...")

    except ParserError as error:
        logging.warning("ParserError : %s", error)
        return return_infos(error=True,
                            message=random.choice(
                                PARSER_FAILURE_MESSAGES))

    try:
        gmaps_api_request = GmapsApiRequest(parser.query_relevant_words)
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng
        logging.debug("Here are latitude and longitude returned by GoogleMaps \
API : %s, %s", lat, lng)

    except GmapsApiError as error:
        logging.warning("GmapsApiError : %s", error)
        return return_infos(error=True,
                            message=random.choice(ADDRESS_FAILURE_MESSAGES))

    try:
        mediawiki_api_request = MediaWikiApiRequest(lat, lng)

    except MediaWikiApiError as error:
        logging.warning("MediaWikiError : %s", error)
        return return_infos(address=address, lat=lat, lng=lng,
                            summary_message=random.choice(
                                SUMMARY_FAILURE_MESSAGES))

    return return_infos(address=address, lat=lat, lng=lng,
                        summary=mediawiki_api_request.summary)
