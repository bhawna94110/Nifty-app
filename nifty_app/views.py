from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DailyPriceRecordSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import DefaultPagination
from .models import DailyPriceRecord
from .filters import DailyPriceRecordFilter


class DailyPriceRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DailyPriceRecord.objects.all()
    serializer_class = DailyPriceRecordSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = DailyPriceRecordFilter
    pagination_class = DefaultPagination
    search_fields = ['open_price', 'high_price', 'low_price', 'close_price', 'shares_traded', 'turnover']


    

