from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Meal(models.Model):
    meal_date = models.DateField(unique=True)
    meal_choice = models.CharField(max_length=200)