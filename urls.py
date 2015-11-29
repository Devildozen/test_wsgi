import views
import re


# compile url regexp
def url(url, view):
    return (re.compile(url, re.IGNORECASE), view,)


urls = [
    url(r'^/$', views.index),
    url(r'^/test_get/$', views.test_get_view),
    url(r'^/test_post/$', views.test_post_view),
    url(r'^/test_class/$', views.TestView.as_view()),
]
