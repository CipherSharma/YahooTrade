from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from rest_framework.views import APIView
import time 
import datetime
import pandas as pd
import csv

from .models import StockData


# Create your views here.
class DisplayStockData(APIView):
    def get(self,request):

        ticker=['GC=F','USDC-INR','CL=F','^DJI','^IXIC','CAC','DAX','^NSEI']
        names=['Gold', 'USD/INR', 'CrudeOil', 'DOW', 'NASDAQ', 'CAC', 'DAX', 'NIFTY']
        # Gold, USD/INR, Crude Oil, DOW, NASDAQ, CAC, DAX, NIFTY. 
        period1=int(time.mktime((datetime.datetime.now() - datetime.timedelta(days=5)).timetuple()))
        period2=int(time.mktime(datetime.datetime.now().timetuple()))
        interval='1d'
        df=pd.DataFrame()
        for i in ticker:
            QueryString= f'https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
            temp=pd.read_csv(QueryString)
            df=pd.concat([df,temp])

        df.to_csv('test.csv')
        StockData.objects.all().delete()
        with open('test.csv','r') as f:
            reader=csv.reader(f)
            count=0
            for i,row in enumerate(reader):
                if (i==0):
                    pass
                else:
                    row=' '.join(row)
                    row=row.split()
                    if(row[0]=='0'):
                        tempname=names[count]
                        count+=1
                    name=tempname
                    date=row[1]
                    openvalue=float(row[2])
                    high=float(row[3])
                    low=float(row[4])
                    close=float(row[5])
                    adjclose=float(row[6])
                    volume=(row[7])
                    StockData.objects.create(
                        name=name,date=date,open=openvalue,
                        high=high,low=low,close=close,
                        adjclose=adjclose,volume=volume)
        stockdata=StockData.objects.all()

        return render(request,'index.html',{'stockdata':stockdata})
    