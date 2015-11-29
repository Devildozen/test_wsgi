# -*- coding: utf-8 -*-

def my_test_view(environ, start_response):
    body = 'Request type: {}'.format(environ['REQUEST_METHOD'])
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    # start_response(status, headers)
    return (status, headers, body)
    # return [body]