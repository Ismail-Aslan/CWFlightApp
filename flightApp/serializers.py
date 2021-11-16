from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'
        
class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer()
    class Meta:
        model = Reservation
        # fields = [
        #     "flight_id",
        #     "passenger",
        #     "user_id"
        # ]
        fields = "__all__"
        
    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        Passenger.objects.create(**passenger_data)
        print(*validated_data)
        reservation = Reservation.objects.create(passenger= Passenger.objects.get(**passenger_data),**validated_data)
        return reservation

