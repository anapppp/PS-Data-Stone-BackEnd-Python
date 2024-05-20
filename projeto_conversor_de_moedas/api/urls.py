from django.urls import path
from .views import hello_world
app_name = 'api'


urlpatterns = [
    path('api', hello_world)
]
