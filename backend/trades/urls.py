from django.urls import path
from .views import trade_journal_API

urlpatterns = [
    path('tradejournal/', trade_journal_API),
]