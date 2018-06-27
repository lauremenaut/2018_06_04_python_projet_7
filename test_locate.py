#! /usr/bin/env python3
# coding: utf-8

from app.locate import locate
from app.utils.messages import success_messages, summary_messages, end_messages


class TestLocate:
    locate_return = locate("Salut GrandPy ! Est-ce que tu connais, par hasard, l'adresse d'OpenClassrooms ?")

    def test_locate_error(self):
        assert self.locate_return[0] is False

    def test_locate_message(self):
        assert self.locate_return[1] in success_messages

    def test_locate_address(self):
        assert self.locate_return[2] == "7 Cité Paradis, 75010 Paris, France"

    def test_locate_lat(self):
        assert self.locate_return[3] == 48.8747578

    def test_locate_lng(self):
        assert self.locate_return[4] == 2.350564700000001

    def test_locate_summary_message(self):
        assert self.locate_return[5] in summary_messages

    def test_locate_summary(self):
        assert self.locate_return[6] == "L'Hôtel Bourrienne (appelé aussi Hôtel de Bourrienne et Petit Hôtel Bourrienne) est un hôtel particulier du XVIIIe siècle situé au 58 rue d'Hauteville dans le 10e arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le 20 juin 1927. En juillet 2015, il est acheté par l'entrepreneur Charles Beigbeder pour en faire le siège de ses activités d'investissement."

    def test_locate_end_message(self):
        assert self.locate_return[7] in end_messages
