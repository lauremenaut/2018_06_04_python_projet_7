#! /usr/bin/env python3
# coding: utf-8

from flask import render_template

from app import app
from app.form import QueryForm


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QueryForm()
    sentence1 = "Bonjour mon petit, as-tu une question pour moi ?"
    # sentence2 =
    # sentence3 =
    return render_template('index.html', sentence1=sentence1, form=form)
