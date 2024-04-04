from django.db import models

# Create your models here.
class Predict(models.Model):
    appliance = models.CharField(max_length = 20)
    month = models.IntegerField()
    starttime = models.IntegerField()
    fintime = models.IntegerField()
    pred = models.FloatField()

    def __str__(self):
        return self.appliance
