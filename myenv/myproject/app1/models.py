from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True) 
    emp_id = models.CharField(max_length=3,blank=True,null=True) 
    email = models.EmailField(max_length=30, null=True,blank=True)
    phone = models.CharField(max_length=10,blank=True,null=True)

