from django.db import models

class Titanic(models.Model):
	group = models.CharField(max_length=10)
	sex = models.CharField(max_length=10)
	age = models.CharField(max_length=10)
	survived = models.BooleanField()
	freq = models.IntegerField()