from django.db import models
from django.db.models import signals

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class EnvironmentType(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name

class Environment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    environment_type = models.ForeignKey(EnvironmentType, on_delete=models.CASCADE)

