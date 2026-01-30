from rest_framework import serializers
from .models import TradeJournal

class TradeJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeJournal
        fields = '__all__'
