from django import forms
from .models import Manifestation


class ManifestationForm(forms.ModelForm):
    is_public = forms.BooleanField(
        required=False, label='Make public?',
        help_text='Check to share manifestation publicly.'
        )

    class Meta:
        model = Manifestation
        fields = ['title', 'description', 'style_choice', 'is_public', ]
