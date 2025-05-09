from rest_framework import serializers

from accounts.models import User

# Envia o objeto (User) em uma requisição HTTP(API), transformando em JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email'
        )