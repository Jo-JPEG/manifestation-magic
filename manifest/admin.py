from django.contrib import admin
from .models import Manifestation

class PublicNotApprovedFilter(admin.SimpleListFilter):
    title = 'Public but not approved'
    parameter_name = 'public_not_approved'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Yes'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            return queryset.filter(is_public=True, is_approved=False)
        return queryset

def approve_manifestations(modeladmin, request, queryset):
    queryset.update(is_approved=True)
approve_manifestations.short_description = "Approve selected manifestations"

class ManifestationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'owner', 'is_public', 'is_approved')
    list_filter = ('is_public', 'is_approved', PublicNotApprovedFilter)
    actions = [approve_manifestations]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Manifestation, ManifestationAdmin)