from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
