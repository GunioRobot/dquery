from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Toy(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=10)
    color = models.CharField(max_length=100)
    created = models.DateField()
    brand = models.ForeignKey(Brand)
    def __unicode__(self):
        return self.name
