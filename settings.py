# -*- coding: utf-8 -*-
import os

PORT = 8080
HOST = '127.0.0.1'

BASE_PATH = os.getcwd()
URLS = os.path.join(BASE_PATH, 'urls.py')
VIEWS = os.path.join(BASE_PATH, 'views.py')
TEMPLATES = os.path.join(BASE_PATH, 'templates/')
STATIC = os.path.join(BASE_PATH, 'static/')
MEDIA = os.path.join(BASE_PATH, 'media/')

