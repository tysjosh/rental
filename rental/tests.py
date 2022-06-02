from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

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

    def test_create_rental(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.data['name'])

    def test_view_all_rentals(self):
        self.client.post(self.url, self.data, format='json')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def tearDown(self):
        return super().tearDown()


class ReservationTestCase(APITestCase):

    def setUp(self):
        self.rental_url = reverse('rental_listcreate')
        self.reservation_url = reverse('reservation_listcreate')

        self.rental_data = [{
            'name': 'Mobil'
        }]
        self.reservation_data = {
            "checkin": "2022-05-29T09:00:00+03:00",
            "checkout": "2022-05-29T09:00:00+03:00",
            "rental": 1
        }

        return super().setUp()

    def test_create_renservation(self):
        self.client.post(self.rental_url, self.rental_data, format='json')
        response = self.client.post(self.reservation_url, self.reservation_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_view_all_reservations(self):
        response = self.client.get(self.rental_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        return super().tearDown()
