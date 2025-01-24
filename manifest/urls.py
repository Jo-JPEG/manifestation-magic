from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_manifestation, name='create_manifestation'),
    path('manifestation/<int:id>/', views.view_manifestation, name='view_manifestation'),
    # ...existing code...
]
