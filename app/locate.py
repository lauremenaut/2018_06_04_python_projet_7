#! /usr/bin/env python3
# coding: utf-8

import random

from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import success_messages, summary_messages, no_summary_messages, end_messages, failure_messages


def locate(query):

    error = False
    message = random.choice(success_messages)

    parser = Parser(query)

    if not parser.query:
        pass
        # return error, message, address, lat, lng, summary_message, summary, end_message

    gmaps_api_request = GmapsApiRequest(parser.query)
    try:
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng

    except AttributeError:
        error = True
        message = random.choice(failure_messages)
        address = None
        lat = None
        lng = None
        # return error, message, address, lat, lng, summary_message, summary, end_message

    mediawiki_api_request = MediaWikiApiRequest(lat, lng)
    try:
        summary_message = random.choice(summary_messages)
        summary = mediawiki_api_request.summary
    except AttributeError:
        summary_message = random.choice(no_summary_messages)
        summary = None

    end_message = random.choice(end_messages)

    return error, message, address, lat, lng, summary_message, summary, end_message
