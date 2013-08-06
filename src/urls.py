from django.conf.urls import patterns, include, url
from views.user import UserView, UserListView


urlpatterns = patterns('',
    url(r'^users/?$', UserListView.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/?$', UserView.as_view(), name='user-detail'),
)
