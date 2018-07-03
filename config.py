#! /usr/bin/env python3
# coding: utf-8


import os


class Config(object):
    # SECRET_KEY = "]d{<Xh),pyrVD.QY8owh7rNmx0b"
    # GOOGLE_MAPS_API_KEY = "AIzaSyD0CWiofMMeygd25DTranGk2XgJXjGsHfs"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
