# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import settings
import imp


def view_404(environ, start_response):
    status = '404 NOT FOUND'
    body = '<h1>This page not found<h1>'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body,)

def view_500(error):
    status = '500 INTERNAL SERVER ERROR'
    body = '<h2>INTERNAL SERVER ERROR</h2>\n{}'.format(error.message)
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body,)
def application(environ, start_response):
    view = get_view(environ)
    try:
        status, headers, body = view(environ, start_response)
    except Exception, error:
        status, headers, body = view_500(error)
    start_response(status, headers)
    return body


def get_view(environ):
    urls = imp.load_source('urls', settings.URLS).urls
    request_url = environ['PATH_INFO']
    for url in urls:
        if url[0].match(request_url):
            return url[1]
    return view_404


httpd = make_server(
    settings.HOST,
    settings.PORT,
    application,
)
print httpd
httpd.serve_forever()
