from rest_framework import serializers
from .models import TestUser  # assuming you have a User model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestUser
        fields = ['id', 'name', 'email', 'age']