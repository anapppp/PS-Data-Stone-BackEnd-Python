from django.urls import path
from .views import conversor
app_name = 'api'


urlpatterns = [
    path('conversor/', conversor)
]
