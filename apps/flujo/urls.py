from django.urls import path
from apps.flujo import views


urlpatterns = [
    path('home/', views.Home.as_view(),name = 'view_home'),
    #path('home1/', views.Home1.as_view(),name = 'view_home'),
]

