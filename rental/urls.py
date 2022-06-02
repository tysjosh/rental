from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rental import views


urlpatterns = [
    path('rentals/', views.GetPostRentals.as_view(), name='rental_listcreate'),
    path('reservations/', views.GetPostReservations.as_view(), name='reservation_listcreate'),
]


urlpatterns = format_suffix_patterns(urlpatterns)