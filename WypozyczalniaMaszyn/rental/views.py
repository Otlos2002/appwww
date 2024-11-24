from rest_framework import viewsets, status
from .models import Kategoria, Maszyna, Wypozyczenie
from .serializers import KategoriaSerializer, MaszynaSerializer, WypozyczenieSerializer, UserSerializer
from rest_framework.views import APIView
from django.db.models import Count,Sum
from rest_framework.decorators import api_view
from django.db.models.functions import TruncMonth
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Wypozyczenie
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Maszyna
from .serializers import MaszynaSerializer
from rest_framework import generics
from datetime import datetime
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Maszyna
from .serializers import MaszynaSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
class KategoriaViewSet(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer

class KategoriaListCreateView(ListCreateAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    permission_classes = [IsAuthenticated]

class KategoriaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
    permission_classes = [IsAuthenticated]

class MaszynaViewSet(viewsets.ModelViewSet):
    queryset = Maszyna.objects.all()
    serializer_class = MaszynaSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class MaszynaListCreateView(ListCreateAPIView):
    queryset = Maszyna.objects.all()
    serializer_class = MaszynaSerializer
    permission_classes = [IsAuthenticated]


class WypozyczeniaUzytkownikaView(generics.ListAPIView):
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAuthenticated or IsAdminUser]

    def get_queryset(self):
        return Wypozyczenie.objects.filter(uzytkownik=self.request.user)

class WypozyczenieViewSet(viewsets.ModelViewSet):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAuthenticated or IsAdminUser]

class WypozyczenieListView(generics.ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer

class WypozyczenieListCreateView(ListCreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAuthenticated]

class WypozyczenieCreateView(generics.CreateAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uzytkownik=self.request.user)

class WypozyczenieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAuthenticated]

class MaszynaListView(generics.ListAPIView):
    queryset = Maszyna.objects.all()
    serializer_class = MaszynaSerializer
    permission_classes = [IsAuthenticated or IsAdminUser]

class MaszynaCreateView(generics.CreateAPIView):
    queryset = Maszyna.objects.all()
    serializer_class = MaszynaSerializer
    permission_classes = [IsAdminUser]

class MaszynaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Maszyna.objects.all()
    serializer_class = MaszynaSerializer
    permission_classes = [IsAuthenticated]

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({"error": "Brak wymaganych danych"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Użytkownik już istnieje"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"message": "Użytkownik został zarejestrowany"}, status=status.HTTP_201_CREATED)

class ZestawienieMiesieczneView(generics.ListAPIView):
    queryset = Wypozyczenie.objects.all()
    serializer_class = WypozyczenieSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        current_month = datetime.now().month
        current_year = datetime.now().year
        return Wypozyczenie.objects.filter(data_wypozyczenia__month=current_month, data_wypozyczenia__year=current_year)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_rentals = queryset.count()
        total_value = queryset.aggregate(total_value=Sum('cena'))['total_value'] or 0

        return Response({
            'total_rentals': total_rentals,
            'total_value': total_value,
            'data': WypozyczenieSerializer(queryset, many=True).data
        })
@api_view(['GET'])
def zestawienie_miesieczne(request):
    wypozyczenia = (
        Wypozyczenie.objects
        .annotate(month=TruncMonth('data_wypozyczenia'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    return Response(wypozyczenia)

@api_view(['GET'])
def wypozyczenia_uzytkownika(request):
    user = request.user
    wypozyczenia = Wypozyczenie.objects.filter(uzytkownik=user)
    serializer = WypozyczenieSerializer(wypozyczenia, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)



