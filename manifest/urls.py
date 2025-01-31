from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name="manifest/change_password.html", success_url='/success/'), name='change_password'),
    path('success/', views.success, name='success'),  # Add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
