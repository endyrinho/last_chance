from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
from api.models import Companies, Vacancies

def company_list(request):
    companies = Companies.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def one_company(request, company_id):
    try:
        company =




