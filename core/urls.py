"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import home, products, exit, register, hacer_reserva, reservas_list, detalle_guarderia, cancelacion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'), ##Se anade la url con sus respectivas conecciones al html
    path('logout/', exit, name='exit'), #para salir
    path('register/', register, name='register'), #para registrar
    path('hacer_reservas/<int:codigo_guarderia>/', hacer_reserva, name='hacer_reservas'),
    path('lista_reservas/', reservas_list, name='list'),
    path('detalle_guarderia/<int:codigo_guarderia>/', detalle_guarderia, name='detalle_guarderia'),
    path('hacer_reservas/<int:codigo_guarderia>/post/', hacer_reserva, name='hacer_reserva'),
    path('cancelacion/<int:id_reserva>/', cancelacion, name='cancelacion'),
    

]
