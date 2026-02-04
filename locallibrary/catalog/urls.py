from django.urls import path
from . import views

urlpatterns = [
    # Por ahora vacío o con una ruta de prueba
    path('', views.index, name='index'),
]