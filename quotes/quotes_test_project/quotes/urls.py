from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.get_random_quote, name='get_random_quote'),
    path('create/', views.create_quote, name='create_quote'),    
    path('<int:quote_id>/like/', views.like_quote, name='like_quote'),
    path('<int:quote_id>/dislike/', views.dislike_quote, name='dislike_quote'),
    path('manage/', views.manage_quotes, name='manage_quotes'),
    path('<int:quote_id>/edit/', views.edit_quote, name='edit_quote'),
    # path('/delete/')
]
