# Generated by Django 3.1.7 on 2021-04-21 14:53

import django.contrib.auth.base_user
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0010_auto_20210421_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrarium',
            name='owner',
            field=models.CharField(default=django.contrib.auth.base_user.AbstractBaseUser.get_username, max_length=30),
        ),
    ]
