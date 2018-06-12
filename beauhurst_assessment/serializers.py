from django.contrib.auth.models import User

from rest_framework import serializers

from companies.models import Company, Country, Employee, Deal

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'creator', 'date_founded', 'country', 'monitors')
        read_only_fields = ('id', 'name', 'description', 'creator', 'date_founded', 'country')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', 'username', 'email')