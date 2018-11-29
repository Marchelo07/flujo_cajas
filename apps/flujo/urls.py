from django.urls import path
from apps.flujo import views


urlpatterns = [
    path('home/', views.Home.as_view(),name = 'view_home'),

    #Activos
    path('activo/listar/', views.ActivoView.as_view(),name = 'view_activo'),
    path('activo/crear/', views.ActivoCreateView.as_view(),name = 'create_activo'),
    path('activo/editar/<int:pk>/', views.ActivoUpdateView.as_view(),name = 'update_activo'),
    path('activo/eliminar/<int:pk>/', views.ActivoDeleteView.as_view(),name = 'delete_activo'),

    #categoria
    path('categoria/listar/', views.CategoriaView.as_view(),name = 'view_categoria'),
    path('categoria/crear/', views.CategoriaCreateView.as_view(),name = 'create_categoria'),
    path('categoria/editar/<int:pk>/', views.CategoriaUpdateView.as_view(),name = 'update_categoria'),
]

