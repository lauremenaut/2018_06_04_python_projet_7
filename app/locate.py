#! /usr/bin/env python3
# coding: utf-8
import random

from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest
from app.utils.messages import success_messages, failure_messages


def locate(query):

    error = False
    message = random.choice(success_messages)

    parser = Parser(query)

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

    mediawiki_api_request = MediaWikiApiRequest(lat, lng)
    try:
        summary = mediawiki_api_request.summary
    except AttributeError:
        summary = None

    return error, message, address, lat, lng, summary
