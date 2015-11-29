import views
import re


# compile url regexp
def url(url, view):
    return (re.compile(url, re.IGNORECASE), view,)


urls = {
    url(r'^/$', views.index),
    url(r'^/test/([0-9]+)/$', views.my_test_view),
    url(r'^/test_post/$', views.test_post_view),
}
