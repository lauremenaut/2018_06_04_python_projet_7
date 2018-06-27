#! /usr/bin/env python3
# coding: utf-8

import requests

from app.utils.gmaps_API_request import GmapsApiRequest


class TestGmapsApiRequest:

    gmaps_API_request = GmapsApiRequest('piscine Foix')

    def test_get_position_info(self, monkeypatch):
        results = {'address_components':
                   [
                       {'long_name': '1B',
                        'short_name': '1B',
                        'types': ['street_number']},
                       {'long_name': 'Avenue du Général de Gaulle',
                        'short_name': 'Avenue du Général de Gaulle',
                        'types': ['route']},
                       {'long_name': 'Foix',
                        'short_name': 'Foix',
                        'types': ['locality', 'political']},
                       {'long_name': 'Ariège',
                        'short_name': 'Ariège',
                        'types': ['administrative_area_level_2', 'political']},
                       {'long_name': 'Occitanie',
                        'short_name': 'Occitanie',
                        'types': ['administrative_area_level_1', 'political']},
                       {'long_name': 'France',
                        'short_name': 'FR',
                        'types': ['country', 'political']},
                       {'long_name': '09000',
                        'short_name': '09000',
                        'types': ['postal_code']}
                    ],
                   'formatted_address': '1B Avenue du Général de Gaulle, 09000 Foix, France',
                   'geometry':
                       {'location':
                        {'lat': 42.9600983,
                         'lng': 1.609331},
                        'location_type': 'ROOFTOP',
                        'viewport':
                            {'northeast':
                                {'lat': 42.96144728029149,
                                 'lng': 1.610679980291502},
                             'southwest':
                                {'lat': 42.9587493197085,
                                 'lng': 1.607982019708498
                                 }
                             }
                        },
                   'partial_match': True,
                   'place_id': 'ChIJ4cjQNyURrxIRJeaVO4PJ3I8',
                   'types': ['establishment', 'point_of_interest']
                   }

        def mockreturn(request):
            return results

        monkeypatch.setattr(requests, 'get', mockreturn)
        assert self.gmaps_API_request.get_position_info('piscine Foix') == results

"""

{'results':
    [
        {'address_components':
            [
                {'long_name': '1B',
                 'short_name': '1B',
                 'types': ['street_number']},
                {'long_name': 'Avenue du Général de Gaulle',
                 'short_name': 'Avenue du Général de Gaulle',
                 'types': ['route']},
                {'long_name': 'Foix',
                 'short_name': 'Foix',
                 'types': ['locality', 'political']},
                {'long_name': 'Ariège',
                 'short_name': 'Ariège',
                 'types': ['administrative_area_level_2', 'political']},
                {'long_name': 'Occitanie',
                 'short_name': 'Occitanie',
                 'types': ['administrative_area_level_1', 'political']},
                {'long_name': 'France',
                 'short_name': 'FR',
                 'types': ['country', 'political']},
                {'long_name': '09000',
                 'short_name': '09000',
                 'types': ['postal_code']}
            ],
         'formatted_address': '1B Avenue du Général de Gaulle, 09000 Foix, France',
         'geometry':
            {'location':
                {'lat': 42.9600983,
                 'lng': 1.609331},
             'location_type': 'ROOFTOP',
             'viewport':
                {'northeast':
                    {'lat': 42.96144728029149,
                     'lng': 1.610679980291502},
                 'southwest':
                    {'lat': 42.9587493197085,
                     'lng': 1.607982019708498
                     }
                 }
             },
         'partial_match': True,
         'place_id': 'ChIJ4cjQNyURrxIRJeaVO4PJ3I8',
         'types': ['establishment', 'point_of_interest']
         }
    ],
    'status': 'OK'
 }

"""
