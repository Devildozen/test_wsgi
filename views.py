# -*- coding: utf-8 -*-
from base import Response, BaseView

def test_get_view(request):
    body = str(request.data)
    return Response(body=body).response()

def test_post_view(environ, start_response):
    body = '<form method="POST" action="/">' \
           'Some text: <input name="test_input" /><br>' \
           'Some text: <input name="test_input2" /><br>' \
           '<input type="submit" />' \
           '</form>'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body)


def index(environ, start_response):
    body = '\n'.join(['%s: %s' % (key, value) for key, value in sorted(environ.items())])
    length = int(environ.get('CONTENT_LENGTH') or '0')
    body = [
        'The Beggining\n',
        '*' * 30 + '\n',
        environ['wsgi.input'].read(length),
        '\n' + '*' * 30 + '\n',
        body,
        '\n' + '*' * 30 ,
        '\nThe End'
    ]
    content_length = sum([len(s) for s in body])
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(content_length))
    ]
    # body = 'index page'
    # status = '200 OK'
    # headers = [
    #     ('Content-Type', 'text/plain'),
    #     ('Content-Length', str(len(body)))
    # ]
    return Response(body=body, headers=headers).response()
    # return (status, headers, body)
#
class TestView(BaseView):
    def get(self, request):
        body = str(request.data)
        return Response(body=body).response()


class classonlymethod(classmethod):
    def __get__(self, instance, owner):
        if instance is not None:
            raise AttributeError("This method is available only on the view class.")
        return super(classonlymethod, self).__get__(instance, owner)

def call(fun):
    fun(5,2)

class TestCallback():
    @classonlymethod
    def sum(self, a, b):
        print a*b+b

    # def __call__(self, a, b):
    #     self.sum(a,b)

class TC(TestCallback):
    pass