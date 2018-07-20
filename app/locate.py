#! /usr/bin/env python3
# coding: utf-8

""" Sets locate() function (called in query_locate() view function). """

import logging
import random

from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import (ADDRESS_SUCCESS_MESSAGES,
                                PARSER_FAILURE_MESSAGES,
                                ADDRESS_FAILURE_MESSAGES,
                                SUMMARY_SUCCESS_MESSAGES,
                                SUMMARY_FAILURE_MESSAGES,
                                NEXT_QUESTION_MESSAGES)
from app.exceptions import ParserError, GmapsApiError, MediaWikiApiError


def _return_infos(error=False,
                  message=random.choice(ADDRESS_SUCCESS_MESSAGES),
                  address=None,
                  lat=None,
                  lng=None,
                  summary_message=random.choice(SUMMARY_SUCCESS_MESSAGES),
                  summary=None,
                  next_question_message=random.choice(
                      NEXT_QUESTION_MESSAGES)):
    """ Set _return_infos() private method.

    Receive 8 parameters :
    - error : a boolean set to False by default. Switched to True if no
    found address.
    - message : a string randomly chosen in messages list.
    - address : a string set to None by default. Containing the address
    of the searched place if previously returned by Google Maps API.
    - lat : a floating number set to None by default. Containing the
    latitude of the searched place if previously returned by Google Maps
    API.
    - lng : a floating number set to None by default. Containing the
    longitude of the searched place if previously returned by Google
    Maps API.
    - summary_message : a string randomly chosen in messages list.
    - summary : a string set to None by default. Containing informative
    text about the searched place if previously returned by MediaWiki
    API.
    - next_question_message : a string randomly chosen in messages list.
    Return a tuple containing these 8 variables.

    """
    # 'error' variable is True only if no address is returned (in parser
    # failure & address failure cases)
    if error:
        summary_message = None
        next_question_message = None

    return (error, message, address, lat, lng,
            summary_message, summary, next_question_message)


def locate(query):
    """ Set locate() function.

    Receive a string containing user query.
    Use Parser, GmapsApiRequest and MediaWikiApiRequest classes.
    Return a tuple of 8 variables via return_infos() method.

    """
    try:
        # Extract relevant words of user query.
        parser = Parser(query)
        logging.debug("Here are relevant words selected by parser : %s",
                      parser.query_relevant_words)

        if not parser.query_relevant_words:
            raise ParserError("Parser didn't find any relevant word ...")

    except ParserError as error:
        logging.warning("ParserError : %s", error)
        # If no relevant words found, error is True. Neither address,
        # nor summary are returned. End of process.
        return _return_infos(error=True,
                             message=random.choice(
                                 PARSER_FAILURE_MESSAGES))

    try:
        # Ask data to Google Maps Geocoding API.
        gmaps_api_request = GmapsApiRequest(parser.query_relevant_words)
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng
        logging.debug("Here are latitude and longitude returned by GoogleMaps \
API : %s, %s", lat, lng)

    except GmapsApiError as error:
        logging.warning("GmapsApiError : %s", error)
        # If there is no data returned from Google Maps Geocoding API,
        # then error becomes true. Neither address, nor summary are
        # returned. End of process.
        return _return_infos(error=True,
                             message=random.choice(ADDRESS_FAILURE_MESSAGES))

    try:
        # Ask data to MediaWiki API.
        mediawiki_api_request = MediaWikiApiRequest(lat, lng)
        summary = mediawiki_api_request.summary

    except MediaWikiApiError as error:
        logging.warning("MediaWikiError : %s", error)
        # If there is no data returned from MediaWiki API, then only
        # Google Maps data are returned.
        return _return_infos(address=address, lat=lat, lng=lng,
                             summary_message=random.choice(
                                 SUMMARY_FAILURE_MESSAGES))

    # If Parser, GmapsApiRequest & MediaWikiApiRequest return data, then
    # all data are returned.
    return _return_infos(address=address, lat=lat, lng=lng,
                         summary=summary)
