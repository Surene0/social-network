from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# СЕРИАЛИЗАТОР ДЛЯ РЕГИСТРАЦИИ
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'username', 'first_name', 'last_name')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


# СЕРИАЛИЗАТОР ДЛЯ ПОКАЗА ПОЛЬЗОВАТЕЛЯ (ДОБАВЛЯЕМ ЭТОТ КЛАСС)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')