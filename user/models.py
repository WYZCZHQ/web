from django.db import models

# Create your models here.
class Userinfo(models.Model):
    uname=models.CharField(max_length=10,null=False,unique=True)
    upwd = models.CharField(max_length=10, null=False)
class Classinfo(models.Model):
    cname = models.CharField(max_length=10, null=False, unique=True)
class Customer(models.Model):
    name=models.CharField(max_length=10,null=False)
class Order(models.Model):
    name=models.CharField(max_length=10,null=False)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
class Teacher(models.Model):
    name = models.CharField(max_length=10, null=False)
class Student(models.Model):
    name = models.CharField(max_length=10, null=False)
    teachers=models.ManyToManyField(Teacher)