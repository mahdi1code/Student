from django.db import models

# Create your models here.

class student(models.Model):
    Id=models.AutoField(primary_key=True)
    fullname= models.CharField(max_length=300)
    Grade=models.CharField(max_length=500)