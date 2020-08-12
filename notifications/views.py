from django.shortcuts import render, HttpResponse

from django.http import HttpResponse

# Create your views here.
from rest_framework import viewsets
import datetime

from .serializers import MemberSerializer
from .models import Task,TaskTracker


class MemberViewSet(viewsets.ModelViewSet):
    queryset = TaskTracker.objects.all().order_by('email')
    serializer_class = MemberSerializer



def send_notification(request):
    
    return HttpResponse('Notification is sent')