#! /usr/bin/env python3
# coding: utf-8

from app.utils.parser import Parser
from app.utils.gmaps_API_request import GmapsApiRequest
from app.utils.mediawiki_API_request import MediaWikiApiRequest

#  Vérifier les codes : if r.status_code != 200:
#                           return _('Echec de service de localisation')
#  cf. MégaTuto Flask - AJAX


def locate(query):
    # try:
    #     parser = Parser(query)
    # except IndexError:
    #     pass

    parser = Parser(query)
    if parser.query == "":
        return None

    # try:
    #     gmaps_api_request = GmapsApiRequest(parser.query)
    #     address = gmaps_api_request.address
    #     lat = gmaps_api_request.lat
    #     lng = gmaps_api_request.lng
    # except IndexError:
    #     pass

    gmaps_api_request = GmapsApiRequest(parser.query)
    address = gmaps_api_request.address
    lat = gmaps_api_request.lat
    lng = gmaps_api_request.lng

    # try:
    #     mediawiki_wrapper = MediaWikiWrapper(lat, lng)
    #     summary = mediawiki_wrapper.summary
    #     return address, lat, lng, summary

    # except:  # Je ne connais pas le type d'erreur levée ...
    #     pass

    # mediawiki_wrapper = MediaWikiWrapper(lat, lng)
    mediawiki_api_request = MediaWikiApiRequest(lat, lng)
    # summary = mediawiki_wrapper.summary
    summary = mediawiki_api_request.summary
    return address, lat, lng, summary
    # return address, lat, lng, summary, message, error(0 ou 1)
