from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('add_album', views.AddAlbum.as_view(), name='add_album'),
    path('edit_album/<int:pk>/', views.EditAlbum.as_view(), name='edit_album'),
    path('delete_album/<int:id>/', views.DeleteAlbum.as_view(), name='delete_album'),
]
