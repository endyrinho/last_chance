from django.http import JsonResponse, HttpResponse

# Create your views here.
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def one_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json())

def company_vacancy_list(request, company_id):
    vacancies = Vacancy.objects.all()
    vacancy = []
    for vac in vacancies:
        a = vac.to_json()
        if a['company_id'] == company_id:
            vacancy.append(a)

    if len(vacancy):
        return JsonResponse(vacancy, safe=False)
    else:
        return HttpResponse("Error")

def vacancy_list(request):
    vacancies = Vacancy.objects.all
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def one_vacancy(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())

def vacancy_topten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
    vacancy_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancy_json, safe=False)