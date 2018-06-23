#! /usr/bin/env python3
# coding: utf-8

""" Sets GmapsApiRequest class.

GmapsApiRequest class retrieves data from
Google Maps Geocoding API.

"""

import logging
from requests import get

from app import appl


class GmapsApiRequest:

    """ Sets GmapsApiRequest class.

    Consists of xxx (private) methods :
        - __init__()
        - _get

    """

    def __init__(self, query):
        """ GmapsApiRequest constructor.

        xxx

        """
        position_info = self.get_position_info(query)

        if position_info:
            self.address = position_info['formatted_address']
            self.lat = position_info['geometry']['location']['lat']
            self.lng = position_info['geometry']['location']['lng']

    def get_position_info(self, query):
        """ Returns .

        xxx

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
            logging.warning(" GoogleMAps didn't find any matching place ... Error : '{}'".format(e))
            return None


def main():
    gmaps_api_request = GmapsApiRequest("piscine Foix")
    print("Coordonnées GPS : ", gmaps_api_request.lat, gmaps_api_request.lng)
    print("Adresse : ", gmaps_api_request.address)


if __name__ == '__main__':
    main()
