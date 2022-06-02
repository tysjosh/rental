from rest_framework.views import APIView
from rest_framework.response import Response
from rental.models import Rental, Reservation
from rest_framework import status
from rental.serializers import RentalSerializer, ReservationSerializer
# Create your views here.

class GetPostRentals(APIView):
    """
    List all rentals, or create a new rental.
    """
    def get(self, request, format=None):
        rentals = Rental.objects.all()
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPostReservations(APIView):
    """
    List all reservations, or create a new reservation.
    """
    def get(self, request, format=None):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

    def post(self, request):
        if Reservation.objects.filter(rental= request.data['rental']).exists():
            reservation = Reservation.objects.filter(rental= request.data['rental']).order_by("-id")[0]
            request.data['previous_reservation_id'] = reservation.id
            print("hello")

        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
