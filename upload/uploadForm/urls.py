from django.urls import path
from .views import index, RecordView

urlpatterns = [
    path('', index),
    path('records', RecordView.as_view())
]