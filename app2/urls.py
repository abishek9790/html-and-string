from django.urls import path
from app2.views import *
app_name='some1'
urlpatterns=[
    path('first/',first,name='first'),
]