from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create_manifestation, name='create_manifestation'),
    path('manifestation/<slug:slug>/', views.view_manifestation, name='view_manifestation'),
    path('manifestation/edit/<slug:slug>/', views.edit_manifestation, name='edit_manifestation'),
    path('manifestation/delete/<slug:slug>/', views.delete_manifestation, name='delete_manifestation'),
    path('public-manifestations/', views.public_manifestations, name='public_manifestations'),
    path('manifestation/charge/<slug:slug>/', views.charge_manifestation, name='charge_manifestation'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
