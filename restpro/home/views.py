from django.shortcuts import render
from rest_framework import viewsets
from home.models import Company
from home.serializers import companySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = companySerializer