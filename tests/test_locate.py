# #! /usr/bin/env python3
# # coding: utf-8

from app.locate import locate
from app.utils.messages import address_success_messages, parser_failure_messages, address_failure_messages, summary_success_messages, summary_failure_messages, next_question_messages


class TestLocateSuccess:
    locate_return = locate("Bonjour GrandPy, comment ça va ? J'aimerais savoir comment aller au Jardin Botanique de Montréal.")

    def test_locate_error(self):
        assert self.locate_return[0] is False

    def test_locate_message(self):
        assert self.locate_return[1] in address_success_messages

    def test_locate_address(self):
        assert self.locate_return[2] == "Montreal Botanical Garden, 4101 Rue Sherbrooke E, Montréal, QC H1X 2B2, Canada"

    def test_locate_lat(self):
        assert self.locate_return[3] == 45.56000179999999

    def test_locate_lng(self):
        assert self.locate_return[4] == -73.5630089

    def test_locate_summary_message(self):
        assert self.locate_return[5] in summary_success_messages

    def test_locate_summary(self):
        assert self.locate_return[6] == "Le parc Maisonneuve est un grand parc de Montréal situé dans l'arrondissement Rosemont–La Petite-Patrie.\nIl est situé près d'un club de golf et de l'Espace pour la vie, comprenant notamment le Jardin botanique. Il est nommé en l'honneur de Paul Chomedey de Maisonneuve, cofondateur de Montréal.\nDe grands spectacles y sont aussi organisés."

    def test_locate_next_question_message(self):
        assert self.locate_return[7] in next_question_messages


class TestLocateParserFailure:
    locate_return = locate("Je ne sais pas ce que je cherche !")

    def test_locate_error(self):
        assert self.locate_return[0] is True

    def test_locate_message(self):
        assert self.locate_return[1] in parser_failure_messages

    def test_locate_address(self):
        assert self.locate_return[2] is None

    def test_locate_lat(self):
        assert self.locate_return[3] is None

    def test_locate_lng(self):
        assert self.locate_return[4] is None

    def test_locate_summary_message(self):
        assert self.locate_return[5] is None

    def test_locate_summary(self):
        assert self.locate_return[6] is None

    def test_locate_next_question_message(self):
        assert self.locate_return[7] is None


class TestLocateAddressFailure:
    locate_return = locate("Je cherche l'adresse d'Openclassrooms")

    def test_locate_error(self):
        assert self.locate_return[0] is True

    def test_locate_message(self):
        assert self.locate_return[1] in address_failure_messages

    def test_locate_address(self):
        assert self.locate_return[2] is None

    def test_locate_lat(self):
        assert self.locate_return[3] is None

    def test_locate_lng(self):
        assert self.locate_return[4] is None

    def test_locate_summary_message(self):
        assert self.locate_return[5] is None

    def test_locate_summary(self):
        assert self.locate_return[6] is None

    def test_locate_next_question_message(self):
        assert self.locate_return[7] is None


class TestLocateSummaryFailure:
    locate_return = locate("Connais-tu l'Océan Atlantique ?")

    def test_locate_error(self):
        assert self.locate_return[0] is False

    def test_locate_message(self):
        assert self.locate_return[1] in address_success_messages

    def test_locate_address(self):
        assert self.locate_return[2] == "Atlantic Ocean"

    def test_locate_lat(self):
        assert self.locate_return[3] == -14.5994134

    def test_locate_lng(self):
        assert self.locate_return[4] == -28.6731465

    def test_locate_summary_message(self):
        assert self.locate_return[5] in summary_failure_messages

    def test_locate_summary(self):
        assert self.locate_return[6] is None

    def test_locate_next_question_message(self):
        assert self.locate_return[7] in next_question_messages
