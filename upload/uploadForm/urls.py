from django.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^records/', views.RecordView)
]