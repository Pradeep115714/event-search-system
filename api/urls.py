from django.urls import path
from .views import search_events, dashboard

urlpatterns = [
    path('search/', search_events),
    path('dashboard/', dashboard),
]