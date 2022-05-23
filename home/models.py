from email.headerregistry import Address
from django.db import models
import datetime

from django.forms import IntegerField

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=30)
    create_date = models.DateField(default=datetime.date.today())
    direction = models.CharField(max_length=30)
    price = models.FloatField()
    is_active = models.BooleanField(default=False)

    def __str__(self) :
        return f"{self.name}"

class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

    def Meta():
        order = ['name']


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
