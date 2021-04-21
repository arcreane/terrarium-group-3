# Generated by Django 3.1.7 on 2021-04-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0008_auto_20210419_2209'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='HumidityControlUser',
        ),
        migrations.AlterField(
            model_name='terrarium',
            name='climate',
            field=models.CharField(blank=True, choices=[('0', 'NA'), ('1', 'Desert'), ('2', 'Temperate'), ('3', 'Tropical / Semi-Aquatic')], default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='terrarium',
            name='currentHumidity',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='terrarium',
            name='maxHumidity',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='terrarium',
            name='minHumidity',
            field=models.IntegerField(default=''),
        ),
    ]