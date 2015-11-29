# -*- coding: utf-8 -*-

class Response(object):
    def __init__(self, status=None, body=None, headers=None):
        self.status = status or '200 OK'
        self.body = body or ''
        self.headers = headers or self.get_headers()

    def get_headers(self):
        if isinstance(self.body, (str, unicode)):
            content_len = len(self.body)
        elif isinstance(self.body, (list, tuple, set)):
            content_len = sum([len(i) for i in self.body])
        else:
            raise BaseException
        headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(content_len))
        ]
        return headers

    def response(self):
        return (self.status, self.headers, self.body)

class Request(object):
    raw_data = ''
    data = dict()

    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.content_length = int(self.environ.get('CONTENT_LENGTH') or '0')
        self.set_data()

    def set_data(self):
        # get GET/POST data

        if self.method == 'GET':
            self.raw_data = self.environ['QUERY_STRING']
        elif self.method == 'POST':
            self.raw_data = self.environ['wsgi.input'].read(self.content_length)

        query = [query.split('=') for query in self.raw_data.split('&') if query]
        for q in query:
            self.data[q[0]] = q[1]


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
