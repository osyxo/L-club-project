from django.db import models

class Gnev(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    years = models.IntegerField()
    power = models.IntegerField()