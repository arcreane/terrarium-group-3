# Generated by Django 3.1.7 on 2021-04-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('humidityControl', '0009_auto_20210420_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='terrarium',
            name='owner',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.DeleteModel(
            name='HumidityControlUser',
        ),
    ]
