#! /usr/bin/env python3
# coding: utf-8

from app.parser import Parser
from app.gmaps_API_request import GmapsApiRequest
from app.mediawiki_wrapper import MediaWikiWrapper

#  Vérifier les codes : if r.status_code != 200:
#                           return _('Echec de service de localisation')
#  cf. MégaTuto Flask - AJAX


def locate(query):
    try:
        parser = Parser(query)
        print("Mots retenus : ", parser.query)
    except IndexError:
        print("\nDis-moi ça plus clairement s'il te plait !")

    try:
        gmaps_api_request = GmapsApiRequest(parser.query)
        address = gmaps_api_request.address
        lat = gmaps_api_request.lat
        lng = gmaps_api_request.lng
        print("\nOh oui, je connais ! Tu trouveras ça au", address)
    except IndexError:
        print("\nÇa, je ne m'en souviens plus ...")

    try:
        mediawiki_wrapper = MediaWikiWrapper(lat, lng)
        summary = mediawiki_wrapper.summary
        print("\nEn parlant de ça, j'avais une petite chose à te raconter ! ", summary)
        return address, summary

    except:  # Je ne connais pas le type d'erreur levée ...
        print("\nEtrangement, je ne connais aucune anecdote à ce sujet !")
