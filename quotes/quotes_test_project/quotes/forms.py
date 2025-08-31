from django import forms
from django.db import models 
from .models import Quote
from sources.models import Source


class QuoteForm(forms.ModelForm):
    """Форма для создания и изменения цитаты."""

    class Meta:
        model = Quote
        fields = ['source', 'quote_text', 'weight']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-control'}),
            'quote_text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '100'
                }),
        }

    # def __init__(self, *args, **kwargs):
    #     """Переопределение метода для отсеивания источников с 3 цитатами."""
    #     super().__init__(*args, **kwargs)
    
    #     self.fields['source'].queryset = Source.objects.annotate(
    #         quote_count=models.Count('quotes')
    #     ).filter(quote_count__lt=3)

