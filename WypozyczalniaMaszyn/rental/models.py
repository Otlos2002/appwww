from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Maszyna(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    cena_za_dzien = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, related_name='maszyny')

    def __str__(self):
        return self.nazwa

class Wypozyczenie(models.Model):
    maszyna = models.ForeignKey(Maszyna, on_delete=models.CASCADE, related_name='wypozyczenia')
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wypozyczenia')
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.uzytkownik.username} - {self.maszyna.nazwa}"

