from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def admin(request):
    return render(request, 'main/admin.html')


def student(request):
    return render(request, 'main/student.html')

def teacher(request):
    return render(request, 'main/teacher.html')   


