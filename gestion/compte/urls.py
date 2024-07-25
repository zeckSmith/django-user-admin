
from django.urls import path
from .views import *

urlpatterns = [
    path('', homme_view, name="home")
]
