from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            access_token = AccessToken.for_user(user)
            return Response({
                'access': str(access_token),
                'user': UserSerializer(user).data
            })
            # refresh = RefreshToken.for_user(user)
            # user_serializer = UserSerializer(user)
            # return Response({
            #     'refresh': str(refresh),
            #     'access': str(refresh.access_token),
            #     'user': user_serializer.data
            # })
        else:
            return Response({'detail': "Invalid credentials"}, status=401)


class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            'message': 'Welcome to dashboard!',
            'user': user_serializer.data
        }, 200)










def index_page(request):
    return render(request, 'index.html')
# Create your views here.





from rest_framework import viewsets
from .models import Product, Category, User, BotConfiguration, Reviews, OrderItem, RoleChoices, UserActivityLogs, SMSCampaign
from .serializers import ProductSerializer, CategorySerializer, UsersSerializer, BotConfigurationSerializer, ReviewSerializer, OrderItemSerializer, RoleChoicesSerializer, UserActivityLogsSerializer, SMSCampaignSerializer
from rest_framework.views import APIView
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer



class BotConfigurationViewSet(viewsets.ModelViewSet):
    queryset = BotConfiguration.objects.all()
    serializer_class = BotConfigurationSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class RoleChoicesViewSet(APIView):
    def get(self, request):
        roles = [{"key": role.name, "value": role.value} for role in RoleChoices]
        return Response(roles, status=status.HTTP_200_OK)




class UserActivityLogsViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLogs.objects.all().order_by('-created_at')
    serializer_class = UserActivityLogsSerializer


class SMSCampaignViewSet(viewsets.ModelViewSet):
    queryset = SMSCampaign.objects.all()
    serializer_class = SMSCampaignSerializer