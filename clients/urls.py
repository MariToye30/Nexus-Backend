from django.urls import path
from .views import client_list_view

urlpatterns = [
    path('clients/', client_list_view, name='client-list'),
]