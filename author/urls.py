from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='author'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]