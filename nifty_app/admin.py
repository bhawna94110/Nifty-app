import csv
from django.contrib import admin    
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from .models import DailyPriceRecord, Index
from django import forms
from datetime import datetime


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()
    
    
class DailyPriceRecordAdmin(admin.ModelAdmin):
    model = DailyPriceRecord
    list_display = ["date", "open_price", "high_price", "low_price", "close_price", "shares_traded", "turnover", "index"]
    actions = ['export_as_csv']
    
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        fieldnames = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(fieldnames)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in fieldnames])
            
        return response
    
    export_as_csv.short_description = 'Export'
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls
    
    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")
            print("csv_data", csv_data)
            
            for x in csv_data[1:]:
                fields = x.split(",")
                original_date_str = fields[0]
                original_date_obj = datetime.strptime(original_date_str, '%d-%b-%Y')
                formatted_date_str = original_date_obj.strftime('%Y-%m-%d')
                created = DailyPriceRecord.objects.update_or_create(
                    date = formatted_date_str,
                    open_price = fields[1],
                    high_price = fields[2],
                    low_price = fields[3],
                    close_price = fields[4],
                    shares_traded = fields[5],
                    turnover = fields[6],
                    index = Index.objects.get(id=request.POST['index']) 
                )
        form = CsvImportForm()
        data = {"form": form}
        print("data", data)
        return render(request, "admin/csv_upload.html", data)

admin.site.register(DailyPriceRecord, DailyPriceRecordAdmin)
admin.site.register(Index)
