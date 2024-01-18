from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class DailyPriceRecord(models.Model):
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    shares_traded = models.BigIntegerField()
    turnover = models.DecimalField(max_digits=15, decimal_places=2)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - Open: {self.open_price}, High: {self.high_price}, Low: {self.low_price}, Close: {self.close_price}, Shares Traded: {self.shares_traded}, Turnover: {self.turnover}"


