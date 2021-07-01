from django.db import models


# Gold, USD/INR, Crude Oil, DOW, NASDAQ, CAC, DAX, NIFTY. 
Data_Choices = (('Gold','gold'),('USD/INR','usd/inr'),('CrudeOil','crudeoil'),('DOW','dow'),('NASDAQ','nasdaq'),('CAC','cac'),('DAX','dax'),('NIFTY','nifty'))

class StockData(models.Model):
    name = models.CharField(max_length=20,choices=Data_Choices)
    date = models.CharField(max_length=20)
    open= models.FloatField(blank=True)
    high= models.FloatField(blank=True)
    low= models.FloatField(blank=True)
    close = models.FloatField(blank=True)
    adjclose = models.FloatField(blank=True)
    volume = models.BigIntegerField(blank=True)

    def __str__(self):
        return f"{self.name}-{self.date}"
        
