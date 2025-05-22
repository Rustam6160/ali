from django import forms
from .models import NaturePlace

class NaturePlaceForm(forms.ModelForm):
    class Meta:
        model = NaturePlace
        fields = ['title', 'description', 'location', 'image_url']
