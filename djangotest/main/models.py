from django.db import models


class Status(models.Model):
    FarmName = models.CharField('Farm name:', max_length=50)
    MacAddress = models.CharField('Mac Address:', max_length=17)
    Temperature = models.IntegerField('Temperature:')
    Light = models.IntegerField('Light')
    Humidity = models.IntegerField('Humidity:')
    TimeTarget = models.DateTimeField('Time Target:')
    TimeLeft = models.CharField('Time Left:', max_length=50)
    GrowthProcess = models.IntegerField('Growth Process:')
    CheckLine = models.BooleanField('Online:', default=False)
    TimeDelta = models.DateTimeField('TimePass:',  auto_now=False)
    AvailabilityOfWater = models.BooleanField('Availability of water', default=False)
    Mode = models.CharField('Mode:', max_length=50)

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.FarmName


class Mode(models.Model):
    ModeName = models.CharField('ModeName:', max_length=50)
    IWater = models.DurationField('Watering Interval:', default='00:00:00')
    TWater = models.DurationField('Watering Time:', default='00:00:00')
    ILight = models.DurationField('Lighting Interval:', default='00:00:00')
    TLight = models.DurationField('Lighting Time:', default='00:00:00')
    Temperature = models.IntegerField('Temperature:')
    Humidity = models.IntegerField('Humidity:')
    GrowingTime = models.DurationField('GrowingTime:', default='00:00:00')

    def get_absolute_url(self):
        return '/management'

    def __str__(self):
        return self.ModeName