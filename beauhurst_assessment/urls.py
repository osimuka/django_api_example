"""beauhurst_assessment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from beauhurst_assessment import views


router = routers.SimpleRouter()
router.register(r'', views.CompanyListView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/monitoring', views.CurrentlyMonitoredCompany.as_view(), name='currently_monitored'),
    url(r'api/avg_employee', views.AverageEmployeeCount.as_view(), name='average_employee_count'),
    url(r'api/ten_most_recent', views.TenMostRecentCompanies.as_view(), name='top_ten_recent_companies'),
    url(r'api/created_most_companies', views.UserWhoCreatedTheMostCompanies.as_view(), name='user_who_created_most_companies'),
    url(r'^', include(router.urls)),
    url(r'^companies/', include('companies.urls', namespace='companies')),
]
