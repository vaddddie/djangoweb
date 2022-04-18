from django.db import models


class Status(models.Model):
    FarmName = models.CharField('Farm name:', max_length=50, blank=True)
    Temperature = models.FloatField('Temperature:')
    Humidity = models.IntegerField('Humidity:')
    Light = models.IntegerField('Light:')
    TimeLeft = models.DateTimeField('Time Left:')
    GrowthProcess = models.IntegerField('Growth Process:')

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.FarmName
