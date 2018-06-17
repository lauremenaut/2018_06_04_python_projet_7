#! /usr/bin/env python3
# coding: utf-8

from flask import Flask
from config import Config

appl = Flask(__name__)
appl.config.from_object(Config)

from app import routes
