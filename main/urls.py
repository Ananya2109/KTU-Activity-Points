from urllib.parse import urlparse
from django import path
from . import views # . means current file

urlpatterns = [
    path('',views.home, name='home'),
]