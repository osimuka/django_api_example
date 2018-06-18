'''Django REST framework was used for this exercise http://www.django-rest-framework.org/'''
from collections import Counter
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from companies.models import Company, Employee, Deal
from rest_framework import viewsets, exceptions, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_api_example.serializers import CompanySerializer, UserSerializer

class CompanyListView(viewsets.ModelViewSet):

    ''' a list of all the comapnies in the database '''

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'id'


class CurrentlyMonitoredCompany(APIView):

    def get_object(self, id):
        try:
            return Company.objects.get(id=id)
        except Company.DoesNotExist:
            raise Http404

    @method_decorator(login_required)
    def get(self, request, format=None):

        '''Create an API end point which allows authenticated users to see 
         which companies they're currently monitoring.'''


        context = {}

        current = request.user

        queryset = Company.objects.filter(monitors=current.id)

        serializer = CompanySerializer(queryset, many=True)

        context = {'currently_monitoring': serializer.data}

        return Response(context)


    @method_decorator(login_required)
    def post(self, request, format=None):

        '''Create an API end point which allows authenticated users (no need to handle API keys, 
        just assume they're logged in) to pass in the id of a company to monitor.'''

        current = request.user

        # get the company the user wants to monitor (passed in from the post request)
        company = self.get_object(id=request.data)

        # updating a django <ManyToManyField> 
        queryset = company.monitors.add(current.id)

        serializer = CompanySerializer(company, data={'monitor':queryset})

        # validate data ( can only save if validated )
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class UserWhoCreatedTheMostCompanies(APIView):
    '''User who has created the most companies'''

    def get(self, request, format=None):

        # python builtin counter
        counter = Counter()

        for company in Company.objects.all():
            counter[company.creator] += 1

        queryset = max(counter, key=lambda k: counter[k])

        serializer = UserSerializer(queryset, many=False)

        context = {'user_created_most_companies': serializer.data}

        return Response(context)

class AverageDealsRaisedbyCountry(APIView):
    '''Average deal amount raised by country (i.e. deals for companies in those countries)'''

    def get(self, request, format=None):

        amount_raised = 0

        company_count = Company.objects.all().count()

        for d in Deal.objects.all():
            amount_raised += d.amount_raised

        avg_raised = amount_raised/company_count

        context = {'average_amount_raised': avg_raised}

        return Response(context)
