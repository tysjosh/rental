from rest_framework import serializers
from .models import Rental, Reservation


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = [
            'id',
            'name',
        ]

class ReservationSerializer(serializers.ModelSerializer):

    rental_name = serializers.CharField(required=False)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'rental',
            'rental_name',
            'checkin',
            'checkout',
            'previous_reservation_id',
        ]