# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    # Common fields for all users (admin, faculty, students)
    # Add any additional fields required for user management

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to faculty members

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields specific to students

class Activity(models.Model):
    name = models.CharField(max_length=255)
    # Add additional fields for activity details

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to='certificates/')
    is_approved = models.BooleanField(default=False)
    # Add additional fields for certificate details, such as date of submission, event type, etc.

class Points(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    # Add additional fields for points details

