from rest_framework import serializers

from companies.models import Company, Country, Employee, Deal

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'creator', 'date_founded', 'country', 'monitors')
        read_only_fields = ('id', 'name', 'description', 'creator', 'date_founded', 'country', 'monitors')