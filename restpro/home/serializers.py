from rest_framework import serializers
from home.models import Company
#create serializers here

class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields ="__all__"