#! /usr/bin/env python3
# coding: utf-8

""" Set 'appl' variable as an instance of Flask class """

from flask import Flask
# from flask_bootstrap import Bootstrap

from config import Config

appl = Flask(__name__)
# bootstrap = Bootstrap(appl)
appl.config.from_object(Config)

from app import routes
