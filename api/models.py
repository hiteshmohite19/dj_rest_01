from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,null=True)
    mobile = models.IntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True,default=0)
    address=models.TextField(null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    profession=models.CharField(max_length=100)
    current_ogranisation=models.CharField(max_length=100,null=True,blank=True)
    previous_organisation=models.CharField(max_length=100,null=True,blank=True)
    joining_date=models.DateField(null=True,blank=True)

