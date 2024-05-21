from django.urls import path
from .views import exchange

app_name = 'api'

urlpatterns = [
    path('exchange/', exchange)
]
