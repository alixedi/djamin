"""
Djamin is simple. It does not have introspection and other similar tricks that
we get with django-admin. As a result, there is no autodiscover etc. However,
as you may observe, this does not make the API any more complex.
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Put your own urls and views that have nothing to do with djamin below
    # url(r'^home/', 'demo.views.home', name='home'),
    # This is how you bring-in djamin:
    url(r'^bookstore/', include('bookstore.urls')),
)