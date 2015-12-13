# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

import settings
from wsgi import application

print 'Runed server on {}:{}'.format(settings.HOST, settings.PORT)
httpd = make_server(settings.HOST, settings.PORT, application)
httpd.serve_forever()
