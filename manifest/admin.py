from django.contrib import admin
from .models import Manifestation

class ManifestationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Manifestation, ManifestationAdmin)