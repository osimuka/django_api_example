from companies.models import Company, Employee
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

class TenMostRecentCompanies(APIView):
    '''The 10 most recently founded companies'''

    def get(self, request, format=None):

        queryset = Company.objects.order_by('-date_founded')[:10]

        serializer = CompanySerializer(queryset, many=True)

        content = {'top_ten_recent_companies': serializer.data}

        return Response(content)

class AverageEmployeeCount(APIView):
    '''Average employee count'''

    def get(self, request, format=None):

        employee_count = Employee.objects.all().count()

        company_count = Company.objects.all().count()

        avg = employee_count/company_count 

        content = {'average_employee_count': avg}

        return Response(content)

class BreakdownOfNumberOfCompaniesFoundedPerQuarter(APIView):
    '''Breakdown of number of companies founded per quarter for the last five years'''
    pass

class UserWhoCreatedTheMostCompanies(APIView):
    '''User who has created the most companies'''

    def get(self, request, format=None):

        # an empty dictionary to store the values for which user created the most company
        d = {}

        for company in Company.objects.all():

            if company.creator not in d:
                d[company.creator] = 1 # each company atleast has a creator
            else:
                d[company.creator] += 1

        user_created_most_companies = max(d, key=d.get)

        content = {'user_created_most_companies': str(user_created_most_companies)}

        return Response(content)

class UserWithHighestNumberofEmployees(APIView):
    '''User with the greatest total number of employees at all companies they have created'''
    pass

class AverageDealsRaisedbyCountry(APIView):
    '''Average deal amount raised by country (i.e. deals for companies in those countries)'''
    pass