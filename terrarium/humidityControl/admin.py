from django.contrib import admin
from humidityControl.models import Terrarium, Owner, HumidityLog, ValveLog, AnimalToHumidity

admin.site.register(Owner)
admin.site.register(HumidityLog)
admin.site.register(ValveLog)


class AnimalToHumidityAdmin(admin.ModelAdmin):
    list_display = ('specie', 'minHumidity', 'maxHumidity', 'climate')
    list_filter = ('climate', 'minHumidity', 'maxHumidity')


class TerrariumAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'owner')
    list_filter = ('owner', 'animal')


admin.site.register(AnimalToHumidity, AnimalToHumidityAdmin)
admin.site.register(Terrarium, TerrariumAdmin)
