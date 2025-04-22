from rest_framework import serializers
from .models import Product, Category, User, BotConfiguration, Reviews, OrderItem, RoleChoices, UserActivityLogs, SMSCampaign


import re
from django.contrib.auth.models import User
from .models import BadPassword


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def validate_password(self, value):
        errors = []

        if len(value) < 6:
            errors.append("Пароль должен содержать минимум 6 символов.")
        if not re.search(r'[A-Z]', value):
            errors.append("Пароль должен содержать хотя бы одну заглавную букву.")
        if not re.search(r'\d', value):
            errors.append("Пароль должен содержать хотя бы одну цифру.")
        if not re.search(r'[@_]', value):
            errors.append("Пароль должен содержать хотя бы один спецсимвол (@ или _).")
        if BadPassword.objects.filter(password__iexact=value).exists():
            errors.append("Этот пароль слишком распространён. Пожалуйста, выберите другой.")

        if errors:
            raise serializers.ValidationError(errors)

        return value





    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.save()
        return user





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)








class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BotConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotConfiguration
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class RoleChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleChoices
        fields = '__all__'





class UserActivityLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivityLogs
        fields = '__all__'


class SMSCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSCampaign
        fields = '__all__'