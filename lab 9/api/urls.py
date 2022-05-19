from django.urls import path
from api.views import *

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:id>'/, one_company),
    path('companies/<int:id>/vacancies/', company_vacancy_list),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', one_vacancy),
    path('vacancies/top_ten/', vacancy_topten)
]