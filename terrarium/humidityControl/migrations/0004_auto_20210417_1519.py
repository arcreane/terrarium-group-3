# Generated by Django 3.1.7 on 2021-04-17 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0003_auto_20210417_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='terrarium',
            name='climate',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='terrarium',
            name='currentHumidity',
            field=models.IntegerField(default='NA', max_length=3),
        ),
        migrations.AddField(
            model_name='terrarium',
            name='maxHumidity',
            field=models.IntegerField(default='NA', max_length=3),
        ),
        migrations.AddField(
            model_name='terrarium',
            name='minHumidity',
            field=models.IntegerField(default='NA', max_length=3),
        ),
    ]