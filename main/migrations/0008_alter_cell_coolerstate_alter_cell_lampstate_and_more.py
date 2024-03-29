# Generated by Django 4.1 on 2022-12-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_mode_isnode_mode_nextid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='CoolerState',
            field=models.IntegerField(default=2, verbose_name='Cooler state:'),
        ),
        migrations.AlterField(
            model_name='cell',
            name='LampState',
            field=models.IntegerField(default=2, verbose_name='Lamp state:'),
        ),
        migrations.AlterField(
            model_name='cell',
            name='PumpState',
            field=models.IntegerField(default=2, verbose_name='Pump state:'),
        ),
    ]
