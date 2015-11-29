# -*- coding: utf-8 -*-

def my_test_view(environ, start_response):
    body = 'Request type: {}'.format(environ['REQUEST_METHOD'])
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body)

def test_post_view(environ, start_response):
    body = '<form method="POST" action="/">' \
           'Some text: <input name="test_input" />' \
           '</form>'
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(body)))
    ]
    return (status, headers, body)


def index(environ, start_response):
    body = '\n'.join(['%s: %s' % (key, value) for key, value in sorted(environ.items())])
    body = [
        'The Beggining\n',
        '*' * 30 + '\n',
        environ['wsgi.input'].read(),
        '*' * 30 + '\n',
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
    return (status, headers, body)