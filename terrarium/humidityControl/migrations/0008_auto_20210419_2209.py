# Generated by Django 3.1.7 on 2021-04-19 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0007_auto_20210419_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]