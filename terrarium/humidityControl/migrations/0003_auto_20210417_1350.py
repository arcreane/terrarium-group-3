# Generated by Django 3.1.7 on 2021-04-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0002_auto_20210329_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valvelog',
            name='actionRequested',
            field=models.CharField(blank=True, choices=[('0', 'Close'), ('1', 'Open')], default='0', help_text="Valve action requested to the terrarium's valve", max_length=1),
        ),
    ]