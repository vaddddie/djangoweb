from django.db import models


class Status(models.Model):
    FarmName = models.CharField('Farm name:', max_length=50)
    Temperature = models.FloatField('Temperature:',blank=True)
    Humidity = models.IntegerField('Humidity:')
    Light = models.IntegerField('Light:')
    TimeLeft = models.DateTimeField('Time Left:')
    GrowthProcess = models.IntegerField('Growth Process:')

    def __str__(self):
        return self.FarmName
