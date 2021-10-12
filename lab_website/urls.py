from django.urls import path
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('news/', NewsList, name='news'),
    path('news/<int:pk>/', NewsDetail.as_view()),
    path('tech-report/', TechList.as_view(), name='tech_report'),
    path('tech-report/<int:pk>/', TechDetail.as_view()),
    path('tech-report/select-date', tech_select_date, name='tech_select_date'),
    path('tech-report/keyword-research', tech_keyword_research, name='tech_keyword_research'),
    path('obser-report/', ObserList.as_view(), name='obser_report'),
    path('obser-report/<int:pk>/', ObserDetail.as_view()),
    path('obser-report/select-date', obser_select_date, name='obser_select_date'),
    path('obser-report/keyword-research', obser_keyword_research, name='obser_keyword_research'),
    path('contact/', contact, name='contact'),
]
