from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('add_musician/', views.AddMusician.as_view(), name='add_musician'),
    path('edit_musician/<int:id>/', views.EditMusician.as_view(), name='edit_musician'),
    #path('add_musician/', views.add_musician, name='add_musician'),
]