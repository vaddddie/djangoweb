from django.db import models


class Status(models.Model):
    FarmName = models.CharField('Farm name:', max_length=50)
    MacAddress = models.CharField('Mac Address:', max_length=17)
    Temperature = models.IntegerField('Temperature:')
    Humidity = models.IntegerField('Humidity:')
    Light = models.IntegerField('Light:')
    TimeTarget = models.DateTimeField('Time Target:')
    TimeLeft = models.CharField('Time Left:', max_length=50)
    GrowthProcess = models.IntegerField('Growth Process:')
    CheckLine = models.BooleanField('Online:', default=False)
    TimeDelta = models.DateTimeField('TimePass:',  auto_now=False)
    AvailabilityOfWater = models.BooleanField('Availability of water', default=False)
    Mode = models.CharField('Mode:', max_length=50)
    Working = models.BooleanField('Working:', default=False)

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.FarmName


class Mode(models.Model):
    ModeName = models.CharField('ModeName:', max_length=50)
    IWater = models.IntegerField('Watering Interval:')
    TWater = models.IntegerField('Watering Time:')
    ILight = models.IntegerField('Lighting Interval:')
    TLight = models.IntegerField('Lighting Time:')
    Temperature = models.IntegerField('Temperature:')
    Humidity = models.IntegerField('Humidity:')

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.ModName