from django.urls import path
from .views import company_list, one_company, company_vacancy_list, vacancy_list,one_vacancy, vacancy_topten

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:company_id>/', one_company),
    path('companies/<int:company_id>/vacancies/', company_vacancy_list),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', one_vacancy),
    path('vacancies/top_ten/', vacancy_topten)
]