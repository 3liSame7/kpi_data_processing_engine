from rest_framework import viewsets
from .models import KPI, AssetKPI
from .serializers import KPISerializer, AssetKPISerializer
from django.http import HttpResponse


class KPIViewSet(viewsets.ModelViewSet):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer

class AssetKPIViewSet(viewsets.ModelViewSet):
    queryset = AssetKPI.objects.all()
    serializer_class = AssetKPISerializer
    
def home(request):
    return HttpResponse("Welcome to the KPI API. Go to /swagger/ for API documentation.")
