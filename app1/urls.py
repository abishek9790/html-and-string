from django.urls import path
from app1.views import *
app_name='some'
urlpatterns=[
    path('funa/',funa,name='funa'),
    path('funb/',funb,name='funb'),
]