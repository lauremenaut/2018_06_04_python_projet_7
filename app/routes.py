#! /usr/bin/env python3
# coding: utf-8

""" Set index() & query_locate() view functions """

import logging

from flask import render_template, jsonify

from app import appl
from app.form import QueryForm
from app.locate import locate

logging.basicConfig(filename="log.log", level=logging.DEBUG,
                    format='%(asctime)s -- %(name)s -- %(levelname)s -- \
%(message)s')


@appl.route('/', methods=['GET', 'POST'])
@appl.route('/index', methods=['GET', 'POST'])
def index():
    """ Set index() view function.

    Use QueryForm class & GOOGLE_MAPS_API_KEY from config.
    Render template returning HTML.

    """
    form = QueryForm()
    key = appl.config['GOOGLE_MAPS_API_KEY']
    return render_template('index.html', form=form, key=key)


@appl.route('/locate', methods=['POST'])
def query_locate():
    """ Set query_locate() view function.

    Use QueryForm class.
    Return data from locate() function, in JSON format.

    """
    form = QueryForm()
    return jsonify({'localisation': locate(form.query.data)})
