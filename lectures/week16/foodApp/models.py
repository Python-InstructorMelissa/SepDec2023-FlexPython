from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    meal = models.CharField(max_length=255)
    servings = models.IntegerField(default=1)
