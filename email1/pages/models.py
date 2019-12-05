from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=25)

    objects = models.Manager

