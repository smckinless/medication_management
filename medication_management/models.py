from django.db import models


class Medication(models.Model):
    name = models.CharField(max_length=256)


class Patient(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    medications = models.ManyToManyField(Medication)