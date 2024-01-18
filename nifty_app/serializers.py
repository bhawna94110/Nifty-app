from rest_framework import serializers
from .models import DailyPriceRecord, Index

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name']
        
class DailyPriceRecordSerializer(serializers.ModelSerializer):
    index = IndexSerializer()
    class Meta:
        model = DailyPriceRecord
        fields = ['id', 'date', 'open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover', 'index']