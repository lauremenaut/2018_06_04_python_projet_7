#! /usr/bin/env python3
# coding: utf-8

""" Set GmapsApiRequest class.

GmapsApiRequest class retrieves data from Google Maps Geocoding API.

"""

import logging

from requests import get

from app import appl
from app.exceptions import GmapsApiError


class GmapsApiRequest:

    """ Set GmapsApiRequest class.

    Consist of 1 private method :
        - _get_position_info()

    """

    def __init__(self, query):
        """ GmapsApiRequest constructor.

        Receive a list of relevant words from user query.
        Set self.address, self.lat and self.lng attributes.

        """
        position_info = self._get_position_info(query)

        if position_info:
            self.address = position_info['formatted_address']
            self.lat = position_info['geometry']['location']['lat']
            self.lng = position_info['geometry']['location']['lng']

    def _get_position_info(self, query):
        """ Set _get_position_info() method.

        Receive the list of relevant words from constructor.
        Send request to Google Maps API.
        Return 'position_info' dictionnary containing address, lat & lng.

        """
        parameters = {
            'address': " ".join(query),
            'key': appl.config['GOOGLE_MAPS_API_KEY']
            }

        response = get('https://maps.googleapis.com/maps/api/geocode/json',
                       params=parameters)
        if response.status_code != 200:
            logging.error(" Localisation failed ... Status code '{}'".format(response.status_code))

        data = response.json()

        try:
            position_info = data['results'][0]
            return position_info

        except IndexError as e:
            logging.warning("IndexError : {}".format(e))
            raise GmapsApiError("GoogleMaps didn't find any matching place ... ({})".format(e))
