from django.conf.urls import url,include 
from . import views



urlpatterns=[
    url(r'^listings', views.index),
    url(r'^update/(?P<anime_id>[0-9]+)$', views.update),
    url(r'^upload/', views.upload)
]



   