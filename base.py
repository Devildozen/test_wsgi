# -*- coding: utf-8 -*-
import os

import settings

class Response(object):
    def __init__(self, status=None, body=None, headers=None):
        self.status = status or '200 OK'
        self.body = body or ''
        self.head = '<ul>' \
                    '<li><a href="/">Index</a></li>' \
                    '<li><a href="/get/">GET</a></li>' \
                    '<li><a href="/post/">POST</a></li>' \
                    '<li><a href="/test_class/">ClassView</a></li>' \
                    '</ul>'
        self.headers = headers or self.get_headers()

    def get_headers(self):
        if isinstance(self.body, (str, unicode)):
            self.body = self.head + self.body
            content_len = len(self.body)
        elif isinstance(self.body, (list, tuple, set)):
            self.body = list(self.head) + list(self.body)
            content_len = sum([len(i) for i in self.body])
        else:
            raise BaseException
        headers = [
            ('Content-Type', 'text/html;charset=utf-8'),
            ('Content-Length', str(content_len))
        ]
        return headers

    def response(self):
        return (self.status, self.headers, self.body)

class Request(object):
    mime_types = {
        'css': 'text/css',
        'js': 'application/javascript',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'png': 'image/png',
        'ttf': 'application/x-font-ttf',
        'html': 'text/html',
    }

    def __init__(self, environ):
        self.raw_data = ''
        self.data = dict()
        self.environ = environ
        self.url = environ['PATH_INFO']
        self.method = environ['REQUEST_METHOD']
        self.content_length = int(self.environ.get('CONTENT_LENGTH') or '0')
        self.set_data()
        self.get_mime_type()

    def set_data(self):
        # get GET/POST data

        if self.method == 'GET':
            self.raw_data = self.environ['QUERY_STRING']
        elif self.method == 'POST':
            self.raw_data = self.environ['wsgi.input'].read(self.content_length)

        query = [query.split('=') for query in self.raw_data.split('&') if query]
        for q in query:
            self.data[q[0]] = q[1]


    def get_mime_type(self):
        # return content type by url, default text/html
        extension = os.path.splitext(self.url)[1].replace('.', '')
        self.mime = self.mime_types.get(extension, 'text/html')


# Magic decorator for can calback class
class classonlymethod(classmethod):
    def __get__(self, instance, owner):
        if instance is not None:
            raise AttributeError("This method is available only on the view class.")
        return super(classonlymethod, self).__get__(instance, owner)


class BaseView(object):
    def get(self, request):
        pass

    def post(self, request):
        pass

    @classonlymethod
    def as_view(cls, **initkwargs):
        def callback_view(request):
            self = cls(**initkwargs)
            return self.dispatch(request)

        return callback_view

    def dispatch(self, request):
        handlers = {
            'GET': self.get,
            'POST': self.post,
        }
        return handlers[request.method](request)

def view_404(request):
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


def static(request):
    file_path = os.path.join(settings.STATIC, request.url.replace('/static/', ''))
    try:
        file = open(file_path, 'rb')
        body = file.read()
    except:
        return view_404(request)
    else:
        headers = [
            ('Content-Type', request.mime),
            ('Content-Length', str(len(body)))
        ]
        return ('200 OK', headers, body,)