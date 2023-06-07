# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    firstname = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    email = models.EmailField()
    #role = models.ForeignKey('Roles', on_delete=models.CASCADE('admin', 'Admin'))

class Roles(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_detail = models.ForeignKey('ClassDetail', on_delete=models.CASCADE, default=False)
    point_scored = models.IntegerField(default=0)

class ClassDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    grad_year = models.ForeignKey('GraduationYear', on_delete=models.CASCADE)

class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_approval_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    activity_point_details = models.ForeignKey('ActivityPoint', on_delete=models.CASCADE,related_name='certificates')

class ActivityPoint(models.Model):
    type = models.CharField(max_length=255)
    point_alloted = models.IntegerField()

class PendingRequest(models.Model):
    #certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    student_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pending_requests')
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    grad_year = models.ForeignKey('GraduationYear', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)

class Branch(models.Model):
    BRANCH_CHOICES = [
        ('csa', 'CSA'),
        ('csb', 'CSB'),
        ('csc', 'CSC'),
        ('csbs', 'CSBS'),
        ('eca', 'ECA'),
        ('ecb', 'ECB'),
        ('eee', 'EEE'),
        ('ebe', 'EBE'),
        ('mech', 'MECH'),
    ]
    branch = models.CharField(max_length=255, choices=BRANCH_CHOICES)

class GraduationYear(models.Model):
    grad_year_choice = [
        ('2024','2024'),
        ('2025','2025'),
        ('2026','2026'),
        ('2027','2027'),
        ('2028','2028'),
        ('2029','2029'),
        ('2030','2030'),
    ]
    grad_year = models.CharField(max_length=255, choices=grad_year_choice)

class Status(models.Model):
    STATUS_CHOICES = [
        ('approved','Approved'),
        ('pending','Pending'),
        ('rejected','Rejected'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
