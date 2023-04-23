from django.db import models

class Fullname(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


