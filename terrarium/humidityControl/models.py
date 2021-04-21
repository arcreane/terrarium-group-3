from django.db import models
from django.urls import reverse


class Terrarium(models.Model):
    owner = models.CharField(max_length=30, default='test')
    nickname = models.CharField(max_length=30)
    animal = models.ForeignKey('AnimalToHumidity', on_delete=models.SET_NULL, null=True)
    CLIMATE_PRESETS = (
        ('0', 'NA'),
        ('1', 'Desert'),
        ('2', 'Temperate'),
        ('3', 'Tropical / Semi-Aquatic')
    )

    climate = models.CharField(
        max_length=1,
        choices=CLIMATE_PRESETS,
        blank=True,
        default='0',
    )
    minHumidity = models.IntegerField(default='')
    maxHumidity = models.IntegerField(default='')
    currentHumidity = models.IntegerField(default='0')

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('terrarium_detail', args=[str(self.id)])





class Owner(models.Model):
    username = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('dashboard', args=[str(self.id)])


class HumidityLog(models.Model):
    terrarium = models.ForeignKey('Terrarium', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    humidity = models.IntegerField(help_text='Humidity value measured at this moment')

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('humidity-detail', args=[str(self.id)])


class ValveLog(models.Model):
    terrarium = models.ForeignKey('Terrarium', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    VALVE_ACTIONS = (
        ('0', 'Close'),
        ('1', 'Open')
    )

    actionRequested = models.CharField(
        max_length=1,
        choices=VALVE_ACTIONS,
        blank=True,
        default='0',
        help_text='Valve action requested to the terrarium\'s valve',
    )

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse('valve-detail', args=[str(self.id)])


class AnimalToHumidity(models.Model):
    specie = models.CharField(max_length=50)
    minHumidity = models.IntegerField()
    maxHumidity = models.IntegerField()

    CLIMATE_PRESETS = (
        ('0', 'NA'),
        ('1', 'Desert'),
        ('2', 'Temperate'),
        ('3', 'Tropical / Semi-Aquatic')
    )

    climate = models.CharField(
        max_length=1,
        choices=CLIMATE_PRESETS,
        blank=True,
        default='0',
    )

    def __str__(self):
        return self.specie

    def get_absolute_url(self):
        return reverse('animalToHumidity-detail', args=[str(self.id)])

    class Meta:
        ordering = ['specie']
