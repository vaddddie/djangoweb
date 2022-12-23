from django.db import models


class Cell(models.Model):
    Name = models.CharField('Name:', max_length=50)
    MacAddress = models.CharField('Mac address:', max_length=17)
    Temperature = models.IntegerField('Temperature:')
    Light = models.BooleanField('Light:')
    Humidity = models.IntegerField('Humidity:')
    # the database for the timer
    TimeTarget = models.DateTimeField('Time target:')
    TimeLeft = models.CharField('Time left:', max_length=50)
    GrowthProcess = models.IntegerField('Growth process:')
    # ==========================
    Online = models.BooleanField('Online:', default=False)
    #  time of the last message
    TimeOfTheLastMessage = models.DateTimeField('Time of the last message:', auto_now=False)
    # ==========================
    AvailabilityOfWater = models.BooleanField('Availability of water', default=False)
    Mode = models.CharField('Mode:', max_length=50)
    # ========States==========
    CoolerState = models.IntegerField('Cooler state:')  # states: 0 - off, 1 - on, 2 - default
    PumpState = models.IntegerField('Pump state:')
    LampState = models.IntegerField('Lamp state:')
    # ========Arrows==========
    Temperature_arrow = models.IntegerField('Arrow on the temperature:', default=0)
    Humidity_arrow = models.IntegerField('Arrow on the humidity:', default=0)
    # ========Logo==========
    Image = models.ImageField('Cell image:', upload_to='cells/%Y-%m-%d/', default='/default_logo/favicon.ico')

    # ======== ==========

    def __str__(self):
        return self.Name


class Mode(models.Model):
    Name = models.CharField('Name:', max_length=50)
    Watering_interval = models.DurationField('Watering Interval:', default='00:00:00')
    Watering_time = models.DurationField('Watering Time:', default='00:00:00')
    Lighting_interval = models.DurationField('Lighting Interval:', default='00:00:00')
    Lighting_time = models.DurationField('Lighting Time:', default='00:00:00')
    Temperature = models.IntegerField('Temperature:')
    Humidity = models.IntegerField('Humidity:')
    GrowingTime = models.DurationField('GrowingTime:', default='00:00:00')

    def __str__(self):
        return self.Name
