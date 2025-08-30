from django.shortcuts import redirect, render
from .forms import SourceForm


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
