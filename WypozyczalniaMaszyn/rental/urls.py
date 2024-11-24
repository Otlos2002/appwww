from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (KategoriaViewSet, MaszynaViewSet,
                    WypozyczenieViewSet, RegisterUserView, zestawienie_miesieczne,
                    wypozyczenia_uzytkownika, WypozyczenieDetailView)

from .views import RegisterView, MaszynaListView, MaszynaCreateView, WypozyczenieListView, WypozyczenieCreateView, ZestawienieMiesieczneView, WypozyczeniaUzytkownikaView
from .views import (MaszynaDetailView, KategoriaListCreateView, KategoriaDetailView, WypozyczenieDetailView, WypozyczenieListCreateView,
                    MaszynaListCreateView, UserListView, UserDetailView)

router = DefaultRouter()
router.register(r'kategorie', KategoriaViewSet)
router.register(r'maszyny', MaszynaViewSet)
router.register(r'wypozyczenia', WypozyczenieViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('zestawienie-miesieczne/', zestawienie_miesieczne, name='zestawienie-miesieczne'),
    path('moje-wypozyczenia/', wypozyczenia_uzytkownika, name='moje-wypozyczenia'),
    path('api/wypozyczenia/', WypozyczenieListView.as_view(), name='wypozyczenia-list'),
    path('api/wypozyczenia/<int:pk>/', WypozyczenieDetailView.as_view(), name='wypozyczenia-detail'),
    path('maszyny/', MaszynaListView.as_view(), name='maszyny-list'),
    path('maszyny/dodaj/', MaszynaCreateView.as_view(), name='maszyny-create'),
    path('wypozyczenia/', WypozyczenieListView.as_view(), name='wypozyczenia-list'),
    path('wypozyczenia/dodaj/', WypozyczenieCreateView.as_view(), name='wypozyczenia-create'),
    path('zestawienie-miesieczne/', ZestawienieMiesieczneView.as_view(), name='zestawienie-miesieczne'),
    path('wypozyczenia/uzytkownik/', WypozyczeniaUzytkownikaView.as_view(), name='wypozyczenia-uzytkownika'),
    # Endpointy dla maszyn
    path('maszyny/', MaszynaListCreateView.as_view(), name='maszyny-list-create'),
    path('maszyny/<int:pk>/', MaszynaDetailView.as_view(), name='maszyny-detail'),
    # Endpointy dla kategorii
    path('kategorie/', KategoriaListCreateView.as_view(), name='kategorie-list-create'),
    path('kategorie/<int:pk>/', KategoriaDetailView.as_view(), name='kategorie-detail'),
    # Endpointy dla wypożyczeń
    path('wypozyczenia/', WypozyczenieListCreateView.as_view(), name='wypozyczenia-list-create'),
    path('wypozyczenia/<int:pk>/', WypozyczenieDetailView.as_view(), name='wypozyczenia-detail'),
    path('uzytkownicy/', UserListView.as_view(), name='user-list'),
    path('uzytkownicy/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

]