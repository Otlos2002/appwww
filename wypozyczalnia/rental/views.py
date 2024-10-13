from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Film, Rental
from .serializers import RegisterSerializer, FilmSerializer, RentalSerializer
from django.shortcuts import render

class RegisterView(generics.CreateAPIView):
    queryset = Film.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class FilmListCreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class RentalListCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class UserRentalsView(generics.ListAPIView):
    serializer_class = RentalSerializer

    def get_queryset(self):
        return Rental.objects.filter(user=self.request.user)


def index(request):
    films = Film.objects.all()  # Pobierz wszystkie filmy z bazy danych
    return render(request, 'rental/index.html', {'films': films})


