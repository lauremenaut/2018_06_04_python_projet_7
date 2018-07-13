#! /usr/bin/env python3
# coding: utf-8

""" Set locate() function """

import random
import logging

from app.exceptions import ParserError, GmapsApiError, MediaWikiApiError
from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import address_success_messages, parser_failure_messages, address_failure_messages, summary_success_messages, summary_failure_messages, next_question_messages


def locate(query):
    """ Set locate() function.

    Receive a string containing user query.
    Use Parser, GmapsApiRequest and MediaWikiApiRequest classes.
    Return a list of 8 variables :
    - error : a boolean, False if an address is found, True else
    - message : a string randomly chosen in messages module
    - address : a string sent back by Google Maps API, or None
    - lat : a floating number sent back by Google Maps API, or None
    - lng : a floating number sent back by Google Maps API, or None
    - summary_message : a string randomly chosen in messages module, or None
    - summary : a string sent back by MediaWiki API, or None
    - next_question_message : a string randomly chosen in messages module, or None

    """
    # 'error' variable is True only if no address is returned (parser failure & address failure)
    def return_infos(error=False, message=random.choice(address_success_messages), address=None, lat=None, lng=None, summary_message=random.choice(summary_success_messages), summary=None, next_question_message=random.choice(next_question_messages)):
        """ Set return_infos() method. """
        if error:
            summary_message = None
            next_question_message = None

        return error, message, address, lat, lng, summary_message, summary, next_question_message

    try:
        parser = Parser(query)
        logging.debug("Here are relevant words selected by parser : {}".format(parser.query_relevant_words))

        if not parser.query_relevant_words:
            raise ParserError("Parser didn't find any relevant word ...")

    except ParserError as e:
        logging.warning("ParserError : {}".format(e))
        return return_infos(error=True, message=random.choice(parser_failure_messages))

    try:
        gmaps_api_request = GmapsApiRequest(parser.query_relevant_words)
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng
        logging.debug("Here are latitude and longitude returned by GoogleMaps API : {}, {}".format(lat, lng))

        if not gmaps_api_request.address:
            logging.warning("GmapsApiError")
            return return_infos(error=True, message=random.choice(address_failure_messages))

    except GmapsApiError as e:
        logging.warning("GmapsApiError : {}".format(e))
        return return_infos(error=True, message=random.choice(address_failure_messages))

    # except AttributeError as e:
    #     logging.warning("AttributeError : {}".format(e))
    #     return return_infos(error=True, message=random.choice(address_failure_messages))

    try:
        mediawiki_api_request = MediaWikiApiRequest(lat, lng)

        if not mediawiki_api_request.summary:
            logging.warning("MediaWikiError")
            return return_infos(address=address, lat=lat, lng=lng, summary_message=random.choice(summary_failure_messages))

    except MediaWikiApiError as e:
        logging.warning("MediaWikiError : {}".format(e))
        return return_infos(address=address, lat=lat, lng=lng, summary_message=random.choice(summary_failure_messages))

    # except AttributeError as e:
    #     logging.warning("AttributeError : {}".format(e))
    #     return return_infos(address=address, lat=lat, lng=lng, summary_message=random.choice(summary_failure_messages))

    return return_infos(address=address, lat=lat, lng=lng, summary=mediawiki_api_request.summary)
