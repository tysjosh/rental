from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
import rental
from rental.models import Rental, Reservation

class RentalTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('rental_listcreate')
        self.data = {
            'name': 'Brew'
        }
        return super().setUp()

    def test_cannot_create_rental_with_no_data(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_rental_returns_201_status_code(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_rental_returns_correct_rental_name(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.data['name'], self.data['name'])

    def test_view_all_rentals(self):
        Rental.objects.create(name='Brew')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        return super().tearDown()


class ReservationTestCase(APITestCase):

    def setUp(self):
        self.rental_url = reverse('rental_listcreate')
        self.reservation_url = reverse('reservation_listcreate')
        self.rental_data = [
            {'name': 'Mobil'},
            {'name': 'Brew'},
            {'name': 'Reval'},
        ]

        [self.client.post(self.rental_url, data, format='json') for data in self.rental_data]

        return super().setUp()

    def test_create_reservation_returns_201_status_code(self):
        reservation_data = {
            "checkin": "2022-05-31",
            "checkout": "2022-06-01",
            "rental": 1
        }
        response = self.client.post(self.reservation_url, reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_returns_correct_rental_name(self):
        reservation_data = {
            "checkin": "2022-05-29T09:00:00+03:00",
            "checkout": "2022-05-29T09:00:00+03:00",
            "rental": 1
        }
        response = self.client.post(self.reservation_url, reservation_data, format='json')
        self.assertEqual(response.data['rental_name'], self.rental_data[0]['name'])


    def test_previous_reservation_id_should_be_none(self):
        reservation_data_1 = {
            "checkin": "2022-05-29T09:00:00+03:00",
            "checkout": "2022-05-29T09:00:00+03:00",
            "rental": 1
        }
        reservation_data_2 = {
            "checkin": "2022-05-29T09:00:00+03:00",
            "checkout": "2022-05-29T09:00:00+03:00",
            "rental": 2
        }

        response = self.client.post(self.reservation_url, reservation_data_1, format='json')
        self.assertEqual(response.data['previous_reservation_id'], None)

        response = self.client.post(self.reservation_url, reservation_data_2, format='json')
        self.assertEqual(response.data['previous_reservation_id'], None)

    def test_previous_reservation_id_values(self):
        rental_1 = Rental.objects.get(id=1)
        Reservation.objects.create(rental=rental_1, checkin="2022-05-31", checkout="2022-06-01")

        reservation_data_1 = {
            "checkin": "2022-06-29",
            "checkout": "2022-06-29",
            "rental": 1
        }
        response = self.client.post(self.reservation_url, reservation_data_1, format='json')
        self.assertEqual(response.data['previous_reservation_id'], 1)
        reservation_data_2 = {
            "checkin": "2022-06-29",
            "checkout": "2022-06-29",
            "rental": 1
        }
        response = self.client.post(self.reservation_url, reservation_data_2, format='json')
        self.assertEqual(response.data['previous_reservation_id'], 2)

        rental_2 = Rental.objects.get(id=2)
        Reservation.objects.create(rental=rental_2, checkin="2022-05-31", checkout="2022-06-01")
        reservation_data_3 = {
            "checkin": "2022-06-29",
            "checkout": "2022-06-29",
            "rental": 2
        }
        response = self.client.post(self.reservation_url, reservation_data_3, format='json')
        self.assertEqual(response.data['previous_reservation_id'], 4)
    

    def test_view_all_reservations(self):
        response = self.client.get(self.rental_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        return super().tearDown()
