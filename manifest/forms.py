from django import forms
from .models import Manifestation

class ManifestationForm(forms.ModelForm):
    class Meta:
        model = Manifestation
        fields = ['title', 'description', 'style_choice', 'is_public', 'is_approved']
