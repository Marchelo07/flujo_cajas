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
    path('categoria/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(),name = 'delete_categoria'),

    #acredor
    path('acredor/listar', views.AcredorView.as_view(), name='view_acredor_listar'),
    path('acredor/editar/<int:pk>/', views.AcredorUpdateView.as_view(), name='view_acredor_update'),
    path('acredor/crear', views.AcredorCreate.as_view(), name='view_acredor_crear'),

    #Obligaciones
    path('obligaciones/listar', views.ObligacionesView.as_view(), name='view_obligaciones'),
    path('olbigaciones/crear', views.ObligacionesCreateView.as_view(), name= 'create_obligaciones'),
    path('olbigaciones/editar/<int:pk>/', views.ObligacionesUpdateView.as_view(), name='update_obligaciones'),
    path('olbigaciones/eliminar/<int:pk>/', views.ObligacionesDeleteView.as_view(),name = 'delete_obligaciones'),

#Obligaciones
    path('movimientos/listar', views.MovimientosView.as_view(), name='view_movimientos'),
    path('movimientos/crear', views.MovimientosCreateView.as_view(), name= 'create_movimientos'),
    path('movimientos/editar/<int:pk>/', views.MovimientosUpdateView.as_view(), name='update_movimientos'),
    path('movimientos/eliminar/<int:pk>/', views.MovimientosDeleteView.as_view(),name = 'delete_movimientos'),
]

