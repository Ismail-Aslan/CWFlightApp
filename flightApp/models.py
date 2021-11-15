from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Passenger(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField('email address', unique=True)
    phone = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Flight(models.Model):
    flightNumber = models.CharField(max_length=10, unique=True)
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField(blank= True,null=True)
    estimatedTimeOfDeparture = models.TimeField(blank= True,null=True)

    def __str__(self):
        return f'{self.flightNumber} {self.operatingAirlines} {self.departureCity}-{self.arrivalCity} {self.dateOfDeparture}-{self.estimatedTimeOfDeparture}'
    
    
class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="flightId")
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Flight_id: {self.flight_id} Passenger_id: {self.passenger_id}'
