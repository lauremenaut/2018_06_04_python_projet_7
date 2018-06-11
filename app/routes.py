#! /usr/bin/env python3
# coding: utf-8

from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    messages = [
        {
            'name': 'GrandPy',
            'message': 'As-tu une question pour moi mon petit ?'
        },
        {
            'name': 'Toi',
            'message': "Quelle est l'adresse du cinéma le plus proche ?"
        },
        {
            'name': 'GrandPy',
            'message': 'Oh oui, je connais ...'
        }

    ]
    return render_template('index.html', messages=messages)
