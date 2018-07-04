#! /usr/bin/env python3
# coding: utf-8

from flask_wtf import FlaskForm

from wtforms import TextAreaField


class QueryForm(FlaskForm):
    query = TextAreaField("Saisissez ici votre question pour GrandPy Bot :")
