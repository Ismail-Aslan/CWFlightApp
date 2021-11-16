from django.urls import path
from .views import home,FlightList, FlightOperations,ReservationList,ReservationOperations,PassengerList


urlpatterns = [
    path('', home),
    path('flights/', FlightList.as_view()),
    path('flights/<int:id>/', FlightOperations.as_view(), name="detail"),
    path('passenger/', PassengerList.as_view()),
    path('reservations/', ReservationList.as_view()),
    path('reservations/<int:id>/', ReservationOperations.as_view(), name="detail"),
]