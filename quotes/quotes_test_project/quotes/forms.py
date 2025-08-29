from django import forms
from .models import Quote, Source


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
    #         quote_count=models.Count('quote')
    #     ).filter(quote_count__lt=3)


class SourceForm(forms.ModelForm):
    """Форма для создания и изменения источника."""

    class Meta:
        model = Source
        fields = ['title', 'tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.Select(attrs={'class': 'form-control'}),
        }

