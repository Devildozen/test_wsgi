# -*- coding: utf-8 -*-

from base import Response, BaseView
from jinja2 import Template

def test_get_view(request):
    body = '<h4>Test GET request</h4><br>Params: {}'.format(unicode(request.data))
    headers = [
        ('Content-Type', 'text/html;charset=utf-8'),
        ('Content-Length', str(len(body)))
    ]
    return Response(body=body, headers=headers).response()

def test_post_view(request):
    body = '<h4>Test POST request</h4><br>' \
           '<form method="POST" action="/test_class/">' \
           'Some text: <input name="test_input" /><br>' \
           'Some text: <input name="test_input2" /><br>' \
           '<input type="submit" />' \
           '</form>'
    # status = '200 OK'
    # headers = [
    #     ('Content-Type', 'text/html'),
    #     ('Content-Length', str(len(body)))
    # ]
    return Response(body=body).response()
    # return (status, headers, body)


def index(request):
    body = ''.join(['<div><span style="width:150px;">%s:</span> %s</div>' % (key, value) for key, value in sorted(request.environ.items())])
    length = int(request.environ.get('CONTENT_LENGTH') or '0')
    body = [
        '<h4>All environment variables</h4>\n',
        '*' * 30 + '<br>',
        request.environ['wsgi.input'].read(length),
        '<br>' + '*' * 30 + '<br>',
        body,
        '<br>' + '*' * 30 ,
        '<br>The End'
    ]
    content_length = sum([len(s) for s in body])
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(content_length))
    ]
    # body = 'index page'
    # status = '200 OK'
    # headers = [
    #     ('Content-Type', 'text/plain'),
    #     ('Content-Length', str(len(body)))
    # ]
    return Response(body=body).response()
    # return (status, headers, body)
#
class TestView(BaseView):
    def get(self, request):
        body = '<h4>Test ClassView with GET request</h4>' \
               '<br>Params: {}'.format(str(request.data))
        return Response(body=body).response()

    def post(self, request):
        body = '<h4>Test ClassView with POST request</h4>' \
               '<br>Params: {}'.format(str(request.data))
        return Response(body=body).response()


class TestTemplateView(BaseView):
    # русский комент
    def get(self, request):
        template = Template(open('templates/test_template.html', 'r').read())
        body = str(template.render(test_message=u'Вася Doe').encode('utf-8'))
        # body = str(u'Вася'.encode('utf-8'))
        return Response(body=body).response()

# class classonlymethod(classmethod):
#     def __get__(self, instance, owner):
#         if instance is not None:
#             raise AttributeError("This method is available only on the view class.")
#         return super(classonlymethod, self).__get__(instance, owner)
#
# def call(fun):
#     fun(5,2)
#
# class TestCallback():
#     @classonlymethod
#     def sum(self, a, b):
#         print a*b+b
#
#     # def __call__(self, a, b):
#     #     self.sum(a,b)
#
# class TC(TestCallback):
#     pass