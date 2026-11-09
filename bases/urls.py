from django.urls import path
from . import views

urlpatterns = [
 path('', views.listar_aprendices, name='listar_aprendices'),
 path('crear/', views.crear_aprendiz, name='crear_aprendiz'),
 path('editar/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
 path('eliminar/<str:documento>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
 path('buscar/', views.buscar_aprendiz, name='buscar_aprendiz'),
 path('mapa/', views.mapa, name='mapa'),
]