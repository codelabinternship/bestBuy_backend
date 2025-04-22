from rest_framework import serializers
from .models import Variations, PaymentMethods, Branches, Product, Category, User, BotConfiguration, Reviews, OrderItem, RoleChoices, TransactionTypeChoices, UserActivityLogs, SMSCampaign



from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

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
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
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


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'

class PaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields = '__all__'

class VariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variations
        fields = '__all__'