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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

from humidityControl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('homepage/', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('dashboard/', views.Dashboard.as_view(template_name='dashboard.html'), name='dashboard'),
    path('', RedirectView.as_view(url='/homepage/', permanent=True)),
    path('terrarium/<int:pk>', views.TerrariumDetailView.as_view(template_name='terrarium_detail.html'),
         name='terrarium_detail'),
    path('terrariums/', views.TerrariumListView.as_view(template_name='terrarium_list.html'), name='terrarium_list'),
]

urlpatterns += [
    url(r'^terrarium/create/$', views.TerrariumCreate.as_view(template_name='terrarium_form.html'),
        name='terrarium_create'),
    url(r'^terrarium/(?P<pk>\d+)/update/$', views.TerrariumUpdate.as_view(template_name='terrarium_form.html'),
        name='terrarium_update'),
    url(r'^terrarium/(?P<pk>\d+)/delete/$', views.TerrariumDelete.as_view(template_name='terrarium_form.html'),
        name='terrarium_delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
