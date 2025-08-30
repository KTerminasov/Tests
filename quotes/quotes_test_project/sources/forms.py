from django import forms
from .models import Source


class SourceForm(forms.ModelForm):
    """Форма для создания и изменения источника."""

    class Meta:
        model = Source
        fields = ['title', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.Select(attrs={'class': 'form-control'}),
        }