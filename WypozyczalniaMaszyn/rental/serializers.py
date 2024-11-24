from rest_framework import serializers
from .models import Kategoria, Maszyna, Wypozyczenie
from django.contrib.auth.models import User

class KategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoria
        fields = '__all__'

class MaszynaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maszyna
        fields = '__all__'

class WypozyczenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wypozyczenie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user