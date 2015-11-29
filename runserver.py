# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import settings
import imp


def view_404():
    status = '404 NOT FOUND'
    body = '<h1>This page not found<h1>'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body,)


def application(environ, start_response):
    # body = '\n'.join(['%s: %s' % (key, value) for key, value in sorted(environ.items())])
    # body = [
    #     'The Beggining\n',
    #     '*' * 30 + '\n',
    #     body,
    #     '\n' + '*' * 30 ,
    #     '\nThe End'
    # ]
    # content_length = sum([len(s) for s in body])
    # status = '200 OK'
    # response_headers = [
    #     ('Content-Type', 'text/plain'),
    #     ('Content-Length', str(content_length))
    # ]
    view = get_view(environ)
    try:
        status, headers, body = view(environ, start_response)
    except Exception, error:
        status = '500 INTERNAL SERVER ERROR'
        body = error.message
        headers = [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body)))
        ]
    start_response(status, headers)
    return body


def get_view(environ):
    urls = imp.load_source('urls', settings.URLS).urls
    url = environ['PATH_INFO']
    try:
        view = urls[url]
    except KeyError:
        view = view_404
    return view

httpd = make_server(
    settings.HOST,
    settings.PORT,
    application,
)
print httpd
httpd.serve_forever()
