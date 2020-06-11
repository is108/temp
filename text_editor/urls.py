from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_text, name='show_text'),
    path('edit/', views.edit_text, name='edit_text'),
    path('load_image/', views.load_image, name='load_image'),
    path('load_file/', views.load_file, name='load_file'),
    path('show_files/', views.show_files, name='show_files'),
]
