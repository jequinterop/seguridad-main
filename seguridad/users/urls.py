from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('login/', views.user_login, name='login'),  # Login
    path('logout/', views.user_logout, name='logout'),  # Logout
]
