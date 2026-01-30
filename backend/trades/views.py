from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import TradeJournal
from .serializers import TradeJournalSerializer 

@csrf_exempt
def trade_journal_API(request):
    if request.method == "GET":
        trade_journal = TradeJournal.objects.all()
        serializer = TradeJournalSerializer(trade_journal, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif request.method == "POST":
        trade_journal_data = JSONParser().parse(request)
        trade_journal_serializer = TradeJournalSerializer(data=trade_journal_data)
        if trade_journal_serializer.is_valid():
            trade_journal_serializer.save()
            return JsonResponse(trade_journal_serializer.data, status=201)
        return JsonResponse(trade_journal_serializer.errors, status=400)
