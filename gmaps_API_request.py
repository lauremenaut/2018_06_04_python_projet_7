#! /usr/bin/env python3
# coding: utf-8

""" Sets GmapsApiRequest class.

GmapsApiRequest class retrieves data from
Google Maps Geocoding API.

"""

from requests import get

from config import GOOGLE_MAPS_GEOCODING_API_KEY


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
        self.address = position_info['formatted_address']
        self.lat = position_info['geometry']['location']['lat']
        self.lng = position_info['geometry']['location']['lng']

    def get_position_info(self, query):
        """ Returns .

        xxx

        """
        parameters = {
            'address': " ".join(query),
            'key': GOOGLE_MAPS_GEOCODING_API_KEY
            }

        response = get('https://maps.googleapis.com/maps/api/geocode/json',
                       params=parameters)
        data = response.json()
        position_info = data['results'][0]
        return position_info


def main():
    gmaps_api_request = GmapsApiRequest("piscine Foix")
    print("Coordonnées GPS : ", gmaps_api_request.lat, gmaps_api_request.lng)
    print("Adresse : ", gmaps_api_request.address)


if __name__ == '__main__':
    main()
