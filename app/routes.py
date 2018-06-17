#! /usr/bin/env python3
# coding: utf-8

from flask import render_template, jsonify

from app import appl
from app.form import QueryForm
from app.locate import locate


@appl.route('/', methods=['GET', 'POST'])
@appl.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    return render_template('index.html', form=form)


@appl.route('/locate', methods=['POST'])
def query_locate():
    form = QueryForm()
    return jsonify({'localisation': locate(form.query.data)})
