# Generated by Django 4.1.dev20220406104243 on 2022-05-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_mod_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='Mode',
            field=models.CharField(default=123123, max_length=50, verbose_name='Mode:'),
            preserve_default=False,
        ),
    ]
