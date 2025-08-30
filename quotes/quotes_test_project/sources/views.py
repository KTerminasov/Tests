from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SourceForm
from .models import Source


def create_source(request):
    """Создание источника цитат."""

    template = 'sources/create_source.html'

    form = SourceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sources:manage_sources')

    context = {
        'form': form
    }

    return render(request, template, context)


def edit_source(request, source_id):
    """Изменение источника."""

    template = 'sources/edit_source.html'

    source = get_object_or_404(Source, id=source_id)
    form = SourceForm(request.POST or None, instance=source)

    if form.is_valid():
        form.save()
        return redirect('sources:manage_sources')

    context = {
        'form': form
    }

    return render(request, template, context)


def delete_source(request, source_id):
    """Удаление источника"""

    template = 'sources/delete_source.html'

    source = get_object_or_404(Source, id=source_id)

    if request.method == 'POST':
        source.delete()
        return redirect('sources:manage_sources')

    context = {
        'source': source,
    }

    return render(request, template, context)


def manage_sources(request):
    """Управление источниками."""

    template = 'sources/manage_sources.html'

    sources_list = Source.objects.all()

    paginator = Paginator(sources_list, 10)
    page_number = request.GET.get('page')
    sources = paginator.get_page(page_number)

    context = {
        'sources': sources
    }
    
    return render(request, template, context)
