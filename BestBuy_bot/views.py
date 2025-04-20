from django.shortcuts import render



def index_page(request):
    return render(request, 'index.html')
# Create your views here.

from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from .models import SMSCampaign
from .serializers import SMSCampaignSerializer

class SMSCampaignViewSet(viewsets.ModelViewSet):
    queryset = SMSCampaign.objects.all()
    serializer_class = SMSCampaignSerializer
