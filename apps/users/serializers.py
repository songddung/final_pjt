from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'nickname', 'social_provider', 'full_name', 'profile_url',
            'inclination', 'age', 'salary', 'favorite_bank', 'gender', 'occupation'
        ]


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'nickname', 'social_provider', 'full_name', 'profile_url',
            'inclination', 'age', 'salary', 'favorite_bank', 'gender', 'occupation'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)