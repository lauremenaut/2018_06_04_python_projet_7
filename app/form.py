#! /usr/bin/env python3
# coding: utf-8

""" Set QueryForm class (inheriting from FlaskForm) """

from flask_wtf import FlaskForm

from wtforms import TextAreaField


class QueryForm(FlaskForm):
    """ Set 'query' variable as an instance of TextAreaField """
    query = TextAreaField("Vous pouvez saisir ici votre question pour GrandPy Bot et taper sur Entrée pour envoyer :")
