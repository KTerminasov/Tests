from django.shortcuts import render, redirect, get_object_or_404
from .models import Source, Quote
from django.http import JsonResponse
from .forms import SourceForm, QuoteForm
import random
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q, Sum, Count


def get_random_quote(request):
    """Получение случайной цитаты."""

    quotes = list(Quote.objects.all())
    if quotes:
        weights = [quote.weight for quote in quotes]
        quote = random.choices(quotes, weights=weights, k=1)[0]
        quote.views += 1
        quote.save()
    else:
        quote = None

    context = {'quote': quote}

    return render(request, 'quotes/random_quote.html', context)


def create_quote(request):
    """Создание цитаты."""

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_random_quote')
    else:
        form = QuoteForm()

    context = {
        'form': form
    }

    return render(request, 'quotes/create_quote.html', context)


def create_source(request):
    """Создание источника цитат."""

    if request.method == 'POST':
        form = SourceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create_quote') 
    else:
        form = SourceForm()

    context = {
        'form': form
    }

    return render(request, 'quotes/create_source.html', context)


@require_POST
def like_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.likes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes, 'dislikes': quote.dislikes})


@require_POST
def dislike_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    quote.dislikes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes, 'dislikes': quote.dislikes})


def manage_quotes(request):
    """Управление цитатами."""
    quotes_list = Quote.objects.select_related('source')

    paginator = Paginator(quotes_list, 10)
    page_number = request.GET.get('page')
    quotes = paginator.get_page(page_number)
          
    sources = Source.objects.all()
    
    context = {
        'quotes': quotes,
        'sources': sources,       
    }
    
    return render(request, 'quotes/manage_quotes.html', context)


def edit_quote(request, quote_id):
    """Изменение цитаты."""

    template = 'quotes/edit_quote.html'
    quote = get_object_or_404(Quote, id=quote_id)

    if request.method == 'POST':
        edited_data = request.POST.copy()
        edited_data['source'] = quote.source.id
        form = QuoteForm(edited_data, instance=quote)
    else:
        form = QuoteForm(instance=quote)

    if form.is_valid():
        form.save()
        return redirect('get_random_quote')    

    context = {'form': form, 'quote': quote}

    return render(request, template, context)

