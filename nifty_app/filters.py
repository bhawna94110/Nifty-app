from django_filters.rest_framework import FilterSet
from .models import DailyPriceRecord

class DailyPriceRecordFilter(FilterSet):
  class Meta:
    model = DailyPriceRecord
    fields = {
      'date': ['gt', 'lt']
    }