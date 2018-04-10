from django.conf.urls import url,include 
from .views import index, update 



urlpatterns=[
    url(r'^listings', index),
    #url(r'^detail', detail),
    url(r'^update/(?P<anime_id>[0-9]+)$', update),
    # path('', index),
    # path('records', RecordView.as_view())
]
   # path('newanime', index),
  #  path('records', RecordView.as_view())



   