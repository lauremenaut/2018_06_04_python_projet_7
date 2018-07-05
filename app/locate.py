#! /usr/bin/env python3
# coding: utf-8

import random
import logging

from app.exceptions import ParserError, GmapsApiError, MediaWikiApiError
from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import success_messages, parser_failure_messages, address_failure_messages, summary_messages, summary_failure_messages, end_messages


def locate(query):

    error = False
    message = random.choice(success_messages)
    summary_message = random.choice(summary_messages)
    end_message = random.choice(end_messages)

    try:
        parser = Parser(query)
        logging.debug("Here are relevant words selected by parser : {}".format(parser.query))

        if not parser.query:
            raise ParserError("Parser didn't find any relevant word ...")

    except ParserError as e:
        logging.warning("ParserError : {}".format(e))
        error = True
        message = random.choice(parser_failure_messages)
        address = None
        lat = None
        lng = None
        summary_message = None
        summary = None
        end_message = None
        return error, message, address, lat, lng, summary_message, summary, end_message

    try:
        gmaps_api_request = GmapsApiRequest(parser.query)
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng
        logging.debug("Here are latitude and longitude returned by GoogleMaps API : {}, {}".format(lat, lng))

        if gmaps_api_request is None:
            raise GmapsApiError("GoogleMaps didn't find any matching place ...")

    except GmapsApiError as e:
        logging.warning("GmapsApiError  {}".format(e))
        error = True
        message = random.choice(address_failure_messages)
        address = None
        lat = None
        lng = None
        summary_message = None
        summary = None
        end_message = None
        return error, message, address, lat, lng, summary_message, summary, end_message

    except AttributeError as e:
        logging.warning("AttributeError : {}".format(e))
        error = True
        message = random.choice(address_failure_messages)
        address = None
        lat = None
        lng = None
        summary_message = None
        summary = None
        end_message = None
        return error, message, address, lat, lng, summary_message, summary, end_message

    try:
        mediawiki_api_request = MediaWikiApiRequest(lat, lng)
        summary = mediawiki_api_request.summary

        if not mediawiki_api_request:
            raise MediaWikiApiError("MediaWiki didn't find any matching article ...")

    except MediaWikiApiError as e:
        logging.warning("MediaWikiError : {}".format(e))
        summary_message = random.choice(summary_failure_messages)
        summary = None

    except AttributeError as e:
        logging.warning("AttributeError : {}".format(e))
        summary_message = random.choice(summary_failure_messages)
        summary = None

    return error, message, address, lat, lng, summary_message, summary, end_message
