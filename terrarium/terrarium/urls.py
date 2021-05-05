"""terrarium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import SAFE_METHODS
from rest_framework import routers, serializers, viewsets, permissions
from humidityControl.models import Terrarium, Owner, HumidityLog, ValveLog, AnimalToHumidity

#class AnimalToHumiditySerializerCustom(serializers.ModelSerializer):
#    class Meta:
#        model = AnimalToHumidity
#        fields = ['id', 'minHumidity']

class TerrariumSerializer(serializers.ModelSerializer):
#    animal = AnimalToHumiditySerializerCustom(read_only=True)
    
    class Meta:
        model = Terrarium
        fields = '__all__'
        depth = 1

class TerrariumSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Terrarium
        fields = '__all__'

# ViewSets define the view behavior.
class TerrariumViewSet(viewsets.ModelViewSet):
#    queryset = Terrarium.objects.all()
#    serializer_class = TerrariumSerializer
    permission_classes=[permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return TerrariumSerializerWrite
        return TerrariumSerializer

    def get_queryset(self):
        return Terrarium.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        #animal = get_object_or_404(animal, idanimal=self.request.data.get('idanimal'))
        serializer.save(owner=self.request.user)
        #serializer.data.owner = self.request.user
        #super(TerrariumViewSet, self).perform_create(serializer)

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


# ViewSets define the view behavior.
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class HumidityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityLog
        fields = '__all__'


# ViewSets define the view behavior.
class HumidityLogViewSet(viewsets.ModelViewSet):
    queryset = HumidityLog.objects.all()
    serializer_class = HumidityLogSerializer


class ValveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValveLog
        fields = '__all__'


# ViewSets define the view behavior.
class ValveLogViewSet(viewsets.ModelViewSet):
    queryset = ValveLog.objects.all()
    serializer_class = ValveLogSerializer


class AnimalToHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalToHumidity
        fields = '__all__'


# ViewSets define the view behavior.
class AnimalToHumidityViewSet(viewsets.ModelViewSet):
    queryset = AnimalToHumidity.objects.all()
    serializer_class = AnimalToHumiditySerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'terrariums', TerrariumViewSet, basename="Terrarium")
router.register(r'owners', OwnerViewSet)
router.register(r'humiditylogs', HumidityLogViewSet)
router.register(r'valvelogs', ValveLogViewSet)
router.register(r'animaltohumidity', AnimalToHumidityViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
]
