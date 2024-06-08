from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Disaster, Alert, Location
from rest_framework import viewsets
from .serializers import DisasterSerializer, AlertSerializer, LocationSerializer


def disaster_info(request):
    return render(request, 'disaster_info/home.html')
    #return HttpResponse ('<h1>Disaster Info Home </h1>')

def about(request):
    return render(request, "disaster_info/about.html")
  
def disaster_list(request):
    disasters = Disaster.objects.all()
    return render(request, 'disaster_info/disaster_list.html', {'disasters': disasters})

def disaster_detail(request, pk):
    disaster = get_object_or_404(Disaster, pk=pk)
    return render(request, 'disaster_info/disaster_detail.html', {'disaster': disaster})

def alert_list(request):
    alerts = Alert.objects.all()
    return render(request, 'disaster_info/alert_list.html', {'alerts': alerts})
   
#API Views
class DisasterViewSet(viewsets.ModelViewSet):
    queryset = Disaster.objects.all()
    serializer_class = DisasterSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    




# Create your views here.
