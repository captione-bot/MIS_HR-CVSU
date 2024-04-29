from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    
class Department(models.Model):
    dept_CHOICES = (
        ('1', 'Department of Computer Studies'),
        ('2', 'Department of Criminology'),
        ('3', 'Department of Psychology'),
        ('4', 'Department of Arts and Studies'),
        ('5', 'Non-Teaching'),
    )
    person = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='department_relation')
    department = models.CharField(choices=dept_CHOICES, max_length=50)

class Attendance(models.Model):
    person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='attendance_records')
    time_in = models.DateTimeField(null=True, blank=True)
    time_out = models.DateTimeField(null=True, blank=True)
    
class SalaryGrade(models.Model):
    SG_CHOICES = (
        ('1', 'INSTRUCTOR I'),
        ('2', 'INSTRUCTOR II'),
        ('3', 'INSTRUCTOR III'),
        ('4', 'NON-TEACHING'),
    )
    person = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='salary_grade_relation')
    salary_grade = models.CharField(choices=SG_CHOICES, max_length=50)

class PayrollSlip(models.Model):
    month = models.DateField()
    total_hours = models.FloatField(null=True, default=None)
    tax = models.FloatField(null=True, default=None)
    gross_pay = models.FloatField(null=True, default=None)
    daily_rate = models.FloatField(null=True, default=None)
    date_period = models.DateField()
    pay_date = models.DateField()
    deduction = models.FloatField(null=True, default=None)
    salary_grade = models.ManyToManyField(SalaryGrade)

class Requirements(models.Model):
    person = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='requirements')
    resume = models.FileField(upload_to='docs/resume')
    tor = models.FileField(upload_to='docs/tor')
    diploma = models.FileField(upload_to='docs/diploma')
    picture = models.FileField(upload_to='docs/picture')
    tin_id = models.IntegerField()
    medical = models.FileField(upload_to='docs/medical')
    nbi = models.FileField(upload_to='docs/nbi')