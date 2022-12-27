# Generated by Django 4.1 on 2022-11-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name:')),
                ('MacAddress', models.CharField(max_length=17, verbose_name='Mac address:')),
                ('Temperature', models.IntegerField(verbose_name='Temperature:')),
                ('Light', models.IntegerField(verbose_name='Light:')),
                ('Humidity', models.IntegerField(verbose_name='Humidity:')),
                ('TimeTarget', models.DateTimeField(verbose_name='Time target:')),
                ('TimeLeft', models.CharField(max_length=50, verbose_name='Time left:')),
                ('GrowthProcess', models.IntegerField(verbose_name='Growth process:')),
                ('Online', models.BooleanField(default=False, verbose_name='Online:')),
                ('TimeOfTheLastMessage', models.DateTimeField(verbose_name='Time of the last message:')),
                ('AvailabilityOfWater', models.BooleanField(default=False, verbose_name='Availability of water')),
                ('Mode', models.CharField(max_length=50, verbose_name='Mode:')),
                ('CoolerState', models.IntegerField(verbose_name='Cooler state:')),
                ('PumpState', models.IntegerField(verbose_name='Pump state:')),
                ('LampState', models.IntegerField(verbose_name='Lamp state:')),
            ],
        ),
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='Name:')),
                ('Watering_interval', models.DurationField(default='00:00:00', verbose_name='Watering Interval:')),
                ('Watering_time', models.DurationField(default='00:00:00', verbose_name='Watering Time:')),
                ('Lighting_interval', models.DurationField(default='00:00:00', verbose_name='Lighting Interval:')),
                ('Lighting_time', models.DurationField(default='00:00:00', verbose_name='Lighting Time:')),
                ('Temperature', models.IntegerField(verbose_name='Temperature:')),
                ('Humidity', models.IntegerField(verbose_name='Humidity:')),
                ('GrowingTime', models.DurationField(default='00:00:00', verbose_name='GrowingTime:')),
            ],
        ),
    ]