from django.db import models


class Status(models.Model):
    FarmName = models.CharField('Farm name:', max_length=50, blank=True)
    MacAddress = models.CharField('Mac Address:', max_length=17)
    Temperature = models.IntegerField('Temperature:')
    Humidity = models.IntegerField('Humidity:')
    Light = models.IntegerField('Light:')
    TimeLeft = models.DateTimeField('Time Left:')
    GrowthProcess = models.IntegerField('Growth Process:')
    CheckLine = models.BooleanField('Online:', default=False)
    TimeDelta = models.CharField('TimePass:', max_length=100)

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.FarmName
