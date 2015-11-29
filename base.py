# -*- coding: utf-8 -*-

class Response(object):
    def __init__(self, status=None, body=None, headers=None):
        self.status = status or '200 OK'
        self.body = body or ''
        self.headers = headers or self.get_headers()
        return (self.status, self.headers, self.body)

    def get_headers(self):
        if isinstance(self.body, (str, unicode)):
            content_len = len(self.body)
        elif isinstance(self.body, (list, tuple, set)):
            content_len = sum([len(i) for i in self.body])
        else:
            raise 'Wrong body content'
        headers = [
            ('Content-Type', 'text/html'),
            ('Content-Length', str(content_len))
        ]
        return headers
#
# class Request(object):
#     def __init__(self, environ):
#         self.environ = environ
#
#     def set_data(self):
#         # get GET data
#         self.data = dict()
#         query = [query.split('=') for query in self.environ['QUERY_STRING'].split('&')]
#         for q in query:
#             self.data[q[0]] = self.data[q[1]]
#
#
# class BaseView(object):
#     def __init__(self, environ, start_response):
#         handlers = {
#             'GET': self.get,
#             'POST': self.post,
#         }
#         handl = handlers[environ['REQUEST_METHOD']]
#         request = Request(environ)
#         handl()
#
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass

