from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path(
        '',
        views.get_random_quote,
        name='get_random_quote'
    ),
    path(
        'quotes/create/',
        views.create_quote,
        name='create_quote'
    ),
    path(
        'quotes/edit/<int:quote_id>/',
        views.edit_quote,
        name='edit_quote'
    ),
    path(
        'quotes/delete/<int:quote_id>/',
        views.delete_quote,
        name='delete_quote'
    ),
    path(
        'quotes/like/<int:quote_id>/',
        views.like_quote,
        name='like_quote'
    ),
    path(
        'quotes/dislike/<int:quote_id>/',
        views.dislike_quote,
        name='dislike_quote'
    ),
    path(
        'quotes/manage/',
        views.manage_quotes,
        name='manage_quotes'
    ),
    path(
        'quotes/top_quotes/',
        views.get_top_quotes,
        name='get_top_quotes'
    )
]
