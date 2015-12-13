import re

import views
import base

# compile url regexp
def url(url, view):
    return (re.compile(url, re.IGNORECASE), view,)


urls = [
    url(r'^/$', views.index),
    url(r'^/static/[a-z/]+\.(jpe?g)?(png)?(css)?(js)?(gif)?(ttf)?$', base.static),
    url(r'^/get/$', views.test_get_view),
    url(r'^/post/$', views.test_post_view),
    url(r'^/test_class/$', views.TestView.as_view()),
    url(r'^/test_template/$', views.TestTemplateView.as_view()),
]
