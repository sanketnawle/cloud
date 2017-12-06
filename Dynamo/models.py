from django.db import models
# Create your models here.

class Dynamo(models.Model):
    text = models.CharField(max_length=250)


