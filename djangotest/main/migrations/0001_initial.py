# Generated by Django 4.1.dev20220406104243 on 2022-04-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FarmName', models.CharField(blank=True, max_length=50, verbose_name='Farm name:')),
                ('MacAddress', models.CharField(max_length=17, verbose_name='Mac Address:')),
                ('Temperature', models.IntegerField(verbose_name='Temperature:')),
                ('Humidity', models.IntegerField(verbose_name='Humidity:')),
                ('Light', models.IntegerField(verbose_name='Light:')),
                ('TimeTarget', models.DateTimeField(verbose_name='Time Target:')),
                ('TimeLeft', models.CharField(max_length=50, verbose_name='Time Left:')),
                ('GrowthProcess', models.IntegerField(verbose_name='Growth Process:')),
                ('CheckLine', models.BooleanField(default=False, verbose_name='Online:')),
                ('TimeDelta', models.DateTimeField(verbose_name='TimePass:')),
            ],
        ),
    ]
