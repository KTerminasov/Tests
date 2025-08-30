import random

from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from sources.models import Source

from .forms import QuoteForm
from .models import Quote


def get_random_quote(request):
    """Получение случайной цитаты."""

    template = 'quotes/random_quote.html'

    quotes = list(Quote.objects.all())
    if quotes:
        weights = [quote.weight for quote in quotes]
        quote = random.choices(quotes, weights=weights, k=1)[0]
        quote.views += 1
        quote.save()
    else:
        quote = None

    context = {'quote': quote}

    return render(request, template, context)


def create_quote(request):
    """Создание цитаты."""

    template = 'quotes/create_quote.html'

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotes:get_random_quote')
    else:
        form = QuoteForm()

    context = {
        'form': form
    }

    return render(request, template, context)


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
        return redirect('quotes:manage_quotes')

    context = {'form': form, 'quote': quote}

    return render(request, template, context)


def delete_quote(request, quote_id):
    """Удаление цитаты."""

    template = 'quotes/delete_quote.html'

    quote = get_object_or_404(Quote, id=quote_id)

    if request.method == 'POST':
        quote.delete()
        redirect('quotes:manage_quotes')

    context = {
        'quote': quote
    }

    return render(request, template, context)


@require_POST
def like_quote(request, quote_id):
    """Проставление лайка цитате."""
    quote = get_object_or_404(Quote, id=quote_id)
    quote.likes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes, 'dislikes': quote.dislikes})


@require_POST
def dislike_quote(request, quote_id):
    """Проставление дизлайка цитате."""
    quote = get_object_or_404(Quote, id=quote_id)
    quote.dislikes += 1
    quote.save()
    return JsonResponse({'likes': quote.likes, 'dislikes': quote.dislikes})


def manage_quotes(request):
    """Управление цитатами."""

    template = 'quotes/manage_quotes.html'

    quotes_list = Quote.objects.select_related('source').order_by('-weight')

    paginator = Paginator(quotes_list, 10)
    page_number = request.GET.get('page')
    quotes = paginator.get_page(page_number)
      
    sources = Source.objects.all()

    context = {
        'quotes': quotes,
        'sources': sources,       
    }
    
    return render(request, template, context)


def get_top_quotes(request):
    """Получение самых популярных цитат."""

    return HttpResponse('Здесь будут лучшие цитаты.')
