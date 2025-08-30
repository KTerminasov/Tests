from django.urls import path

from . import views

app_name = 'sources'

urlpatterns = [
    path(
        'create/',
        views.create_source,
        name='create_source'
    ),
    path(
        'edit/<int:source_id>/',
        views.edit_source,
        name='edit_source'
    ),
    path(
        'delete/<int:source_id>/',
        views.delete_source,
        name='delete_source'
        ),
    path(
        'manage/',
        views.manage_sources,
        name='manage_sources'
    ),
]
