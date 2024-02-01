from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
