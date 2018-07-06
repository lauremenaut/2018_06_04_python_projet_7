#! /usr/bin/env python3
# coding: utf-8

""" Set Config class (inheriting from 'object') """

import os


class Config(object):
    """ Set private keys recovery """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')
