from django.urls import path
from .views import RegisterView, FilmListCreateView, RentalListCreateView, UserRentalsView, index

urlpatterns = [
    path('', index, name='index'),  # Dodaj tę linię
    path('register/', RegisterView.as_view(), name='register'),
    path('films/', FilmListCreateView.as_view(), name='films'),
    path('rentals/', RentalListCreateView.as_view(), name='rentals'),
    path('my-rentals/', UserRentalsView.as_view(), name='my-rentals'),
]
