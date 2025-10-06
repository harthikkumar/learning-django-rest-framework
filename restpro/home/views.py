from django.shortcuts import render
from rest_framework import viewsets
from home.models import Company,Employee
from home.serializers import companySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = companySerializer

    @action(detail=True,methods=['GET'])
    def employees(self,request,pk=None):
        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company might not exist !! Error company '
            })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer