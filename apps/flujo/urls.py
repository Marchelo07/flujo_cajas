from django.urls import path
from apps.flujo import views


urlpatterns = [
    path('home/', views.Home.as_view(),name = 'view_home'),
    path('home/', views.HomePrueba.as_view(),name = 'view_prueba'),
    path('activo/listar/', views.ActivoView.as_view(),name = 'view_activo'),
    path('activo/crear/', views.ActivoCreateView.as_view(),name = 'create_activo'),
]

