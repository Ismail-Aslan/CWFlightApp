from django.shortcuts import HttpResponse
from .models import Flight,Passenger,Reservation
from .serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from .permissions import IsAdminOrReadOnly, IsAddedByUserOrReadOnly

# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class FlightList(generics.ListCreateAPIView):
    serializer_class = FlightSerializer
    # pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['flightNumber', ]
    ordering_fields = '__all__'
    # permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        queryset = Flight.objects.all()
        flightNumber = self.request.query_params.get('flightNumber')
        if flightNumber is not None:
            queryset = queryset.filter(flightNumber=flightNumber)
        return queryset
    
    
    
class FlightOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    lookup_field="id"
    # permission_classes = [IsAddedByUserOrReadOnly]