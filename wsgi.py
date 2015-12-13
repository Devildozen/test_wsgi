# -*- coding: utf-8 -*-
import settings
import imp
from base import Request, view_404, view_500

def application(environ, start_response):
    # body = 'Request type: {}'.format(environ['QUERY_STRING'])
    # status = '200 OK'
    # headers = [
    #     ('Content-Type', 'text/plain'),
    #     ('Content-Length', str(len(body)))
    # ]
    # start_response(status, headers)
    # return body
    view = get_view(environ)
    # try:
    status, headers, body = view(Request(environ))
    # except Exception, error:
    #     status, headers, body = view_500(error)
    start_response(status, headers)
    return body


def get_view(environ):
    urls = imp.load_source('urls', settings.URLS).urls
    request_url = environ['PATH_INFO']
    for url in urls:
        if url[0].match(request_url):
            return url[1]
    return view_404