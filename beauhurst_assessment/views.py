from companies.models import Company
from rest_framework import viewsets
from rest_framework.decorators import api_view
#from django_filters.rest_framework import DjangoFilterBackend
from beauhurst_assessment.serializers import CompanySerializer

class CompanyListView(viewsets.ModelViewSet):

    '''Create an API end point which allows authenticated users (no need to handle API keys, 
    just assume they're logged in) to pass in the id of a company to monitor.
    Create an API end point which allows authenticated users to see which companies they're currently monitoring.
    '''
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'

class TenMostRecentlyFoundedCompanyView(viewsets.ModelViewSet):
    '''Average employee count'''
    pass

class AverageEmployeeCountView(viewsets.ModelViewSet):
    '''Breakdown of number of companies founded per quarter for the last five years'''
    pass

class NumberOfCompaniesLastFiveYearsView(viewsets.ModelViewSet):
    '''User who has created the most companies'''
    pass

class UserWithHighestNumberofEmployees(viewsets.ModelViewSet):
    '''Average deal amount raised by country (i.e. deals for companies in those countries)'''
    pass

class AverageDealsRaisedbyCountry(viewsets.ModelViewSet):
    '''Average deal amount raised by country (i.e. deals for companies in those countries)'''
    pass