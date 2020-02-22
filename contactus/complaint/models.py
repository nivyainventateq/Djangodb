from django.db import models

class Contacttb(models.Model):
    fname=models.CharField(max_length=30,blank=True,null=True)
    lname=models.CharField(max_length=30,blank=True,null=True)
    place=models.CharField(max_length=30,blank=True,null=True)
    sub=models.CharField(max_length=30,blank=True,null=True)


