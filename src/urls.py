from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'userapi.views.home', name='home'),
)
