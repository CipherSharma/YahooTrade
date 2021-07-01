from django.urls import path,include

from home import views
from .views import DisplayStockData

urlpatterns =[
    path('',DisplayStockData.as_view(), name="home"),
]