from urllib.parse import urlparse
from django.urls import path, include
from . import views # . means current file

urlpatterns = [
    path('',views.index, name='index'),
]