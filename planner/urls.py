from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
#from rest_framework import routers

from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_guest/$', views.add_guest, name='add_guest'),
    url(r'^add_finance/$', views.add_finance, name='add_finance'),
    url(r'^buffet_price/$', views.buffet_price, name='buffet_price'),
    #url(r'^guest_list_api/$', views.GuestsViewSet, name='guest_list_api'),
]