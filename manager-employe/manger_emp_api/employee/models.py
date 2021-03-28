from django.db import models


# Create your models here.
class Employee(models.Model):
    email = models.EmailField(max_length=50, blank='False', default='', unique='True')
    firstname = models.CharField(max_length=50, blank='False', default='')
    lastname = models.CharField(max_length=50, blank='False', default='')
    password = models.CharField(max_length=50, blank='False', default='')
    address = models.CharField(max_length=50, blank='False', default='')
    dob = models.DateField(blank='False', default='')
    company = models.CharField(max_length=50, blank='False', default='')
    mobile = models.CharField(max_length=10, blank='False', default='')
    city = models.CharField(max_length=50, blank='False', default='')
