from django.shortcuts import render
from rest_framework import permissions
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
from .models import *
from .serializers import *

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
    permission_classes = [IsAuthenticated]

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
from .serializers import VariationsSerializer, PaymentMethodsSerializer, OrdersSerializer, ExportHistorySerializer, ChannelPostsSerializer, LoyaltyProgramSerializer, BranchesSerializer, ProductSerializer, CategorySerializer, UsersSerializer, BotConfigurationSerializer, ReviewSerializer, OrderItemSerializer, RoleChoicesSerializer, UserActivityLogsSerializer, SMSCampaignSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
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



class RoleChoicesView(APIView):
    def get(self, request):
        roles = [{"key": role.name, "value": role.value} for role in RoleChoices]
        return Response(roles, status=status.HTTP_200_OK)



class UserActivityLogsViewSet(viewsets.ModelViewSet):
    queryset = UserActivityLogs.objects.all().order_by('-created_at')
    serializer_class = UserActivityLogsSerializer


class SMSCampaignViewSet(viewsets.ModelViewSet):
    queryset = SMSCampaign.objects.all()
    serializer_class = SMSCampaignSerializer


class BranchesViewSet(viewsets.ModelViewSet):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

class PaymentMethodsViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer

class VariationsViewSet(viewsets.ModelViewSet):
    queryset = Variations.objects.all()
    serializer_class = VariationsSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class ExportHistoryViewSet(viewsets.ModelViewSet):
    queryset = ExportHistory.objects.all()
    serializer_class = ExportHistorySerializer

class ChannelPostsViewSet(viewsets.ModelViewSet):
    queryset = ChannelPosts.objects.all()
    serializer_class = ChannelPostsSerializer


class LoyaltyProgramViewSet(viewsets.ModelViewSet):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь и магазин успешно созданы'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
