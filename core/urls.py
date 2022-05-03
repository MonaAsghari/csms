from django.urls import path
from .views import ChargingProcessRating

app_name = 'core'
urlpatterns = [
    path('rate/', ChargingProcessRating.as_view(), name='rate'),
]
