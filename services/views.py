from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.core.files.base import ContentFile
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from .filters import *
from rest_framework.response import Response
from .forms import *
from .models import *
from .serializers import *
from users.models import *
from users.serializers import *


# list available services
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        s = Service.objects.all()
        serializer = ServiceSerialzer(s, many=True)
        return Response(serializer.data)

# list providers list in specific service
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def providers_list(request, pk):
    if request.method == 'GET':
        service = Service.objects.get(pk=pk)
        providers = Profile.objects.filter(is_craftsman=True).filter(service=service)
        serializer = ProviderProfileSerializer(providers, many=True)
        return Response(serializer.data)

# search in providers list
class ProvidersViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.filter(is_craftsman=True)
    serializer_class = ProviderProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProviderFilter
