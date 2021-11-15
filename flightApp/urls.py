from django.urls import path
from .views import home,FlightList, FlightOperations


urlpatterns = [
    path('', home),
    path('flights/', FlightList.as_view()),
    path('flights/<int:id>/', FlightOperations.as_view(), name="detail"),
]