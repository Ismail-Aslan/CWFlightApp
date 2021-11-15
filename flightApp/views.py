from django.shortcuts import HttpResponse
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from .permissions import IsAdminOrReadOnly, IsAddedByUserOrReadOnly

# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class FlightList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    # permission_classes = [IsAdminOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FlightOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    # permission_classes = [IsAddedByUserOrReadOnly]