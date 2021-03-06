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

    Consist of a constructor setting public attributes containing
    position informations sent back by Google Maps API.

    """

    def __init__(self, query):
        """ GmapsApiRequest constructor.

        Receive a list of relevant words from user query.
        Set self.address, self.lat and self.lng public attributes.

        """
        position_info = self._get_position_info(query)

        if position_info:
            self.address = position_info['formatted_address']
            self.lat = position_info['geometry']['location']['lat']
            self.lng = position_info['geometry']['location']['lng']

    def _get_position_info(self, query):
        """ Set _get_position_info() private method.

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
            logging.error(" Localisation failed ... Status code %s",
                          response.status_code)

        data = response.json()

        try:
            position_info = data['results'][0]
            return position_info

        except IndexError as error:
            raise GmapsApiError("GoogleMaps didn't find any matching place ...\
 ({})".format(error))
