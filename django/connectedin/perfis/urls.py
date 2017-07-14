from django.conf.urls import include, url
from django.contrib import admin
from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', views.view, name='view'),
    url(r'^perfis/(?P<perfil_id>\d+)/invite$', views.invite, name='invite'),
    url(r'^convite/(?P<invite_id>\d+)/accept$', views.accept_invite, name='accept')
]


