from urllib.parse import urlparse
from django.urls import path, include
from . import views # . means current file

urlpatterns = [
    path('',views.index, name='index'),
    path('index.html/',views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('student.html/', views.student, name='student'),
    path('teacher.html/', views.teacher, name='teacher')
]