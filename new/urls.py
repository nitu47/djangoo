from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('intro/',intro),
    path('index/',index),
]    