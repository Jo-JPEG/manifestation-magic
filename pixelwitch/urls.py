from django.contrib import admin
from django.urls import path, include
from manifest import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manifest.urls')),
    path('account/', include('account.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]