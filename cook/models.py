from django.db import models


class CookProfile(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    area = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
