from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_manifestation, name='create_manifestation'),
    path('manifestation/<int:id>/', views.view_manifestation, name='view_manifestation'),
    path('manifestation/<int:id>/edit/', views.edit_manifestation, name='edit_manifestation'),
    path('charge/<int:id>/', views.charge_manifestation, name='charge_manifestation'),
    path('manifestation/<int:id>/delete/', views.delete_manifestation, name='delete_manifestation'),
    # ...existing code...
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
