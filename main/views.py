from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    #return HttpResponse("main page")
    return render(request, 'main/index.html')

def admin(request):
    return render(request, 'main/admin')


def student(request):
    return render(request, 'main/student.html')

def teacher(request):
    return render(request, 'main/teacher.html')   


