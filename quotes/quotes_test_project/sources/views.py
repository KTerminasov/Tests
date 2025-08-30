from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import SourceForm


def create_source(request):
    """Создание источника цитат."""

    template = 'sources/create_source.html'

    if request.method == 'POST':
        form = SourceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('quotes:create_quote') 
    else:
        form = SourceForm()

    context = {
        'form': form
    }

    return render(request, template, context)


def edit_source(request, source_id):
    """Изменение источника."""

    return HttpResponse(f'Здесь можно будет изменить источник #{source_id}.')


def delete_source(request, source_id):
    """Удаление источника"""

    return HttpResponse(f'Здесь можно будет удалить источник #{source_id}.')


def manage_sources(request):
    """Управление источниками."""

    return HttpResponse('Здесь будет управление источниками.')
