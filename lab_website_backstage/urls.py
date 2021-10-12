from django.urls import path
from django.contrib.auth.views import LoginView
from django .contrib.auth.decorators import login_required
from .views import *

urlpatterns = [    
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('', login_required(DashList), name='system'),
    path('news/', BacknewsList.as_view(), name='back_news'),
    path('news/<int:pk>/', BacknewsDetail.as_view()),
    path('news/create/', NewsCreate.as_view(), name='create_news'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='update_news'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='delete_news'),
    path('tech-report/', BackTechList.as_view(), name='back_tech_report'),
    path('tech-report/<int:pk>/', BackTechDetail.as_view()),
    path('tech-report/create/', TechCreate.as_view(), name='create_tech_report'),
    path('tech-report/<int:pk>/update/', TechUpdate.as_view(), name='update_tech_report'),
    path('tech-report/<int:pk>/delete/', TechDelete.as_view(), name='delete_tech_report'),
    path('obser-report/', BackObserList.as_view(), name='back_obser_report'),
    path('obser-report/<int:pk>/', BackObserDetail.as_view()),
    path('obser-report/create/', ObserCreate.as_view(), name='create_obser_report'),
    path('obser-report/<int:pk>/update/', ObserUpdate.as_view(), name='update_obser_report'),
    path('obser-report/<int:pk>/delete/', ObserDelete.as_view(), name='delete_obser_report'),
    path('profile/', login_required(profile), name='back_profile'),
    path('profile/change-pw/', ProfileChangePw.as_view(), name='change_pw'),
    path('mail-settings/', BackMailList.as_view(), name='back_mail'),
    path('mail-settings/create/', AddRecipient.as_view(), name='create_recipient'),
    path('mail-settings/<int:pk>/delete/', DeleteRecipient.as_view(), name='delete_recipient'),
    path('account/', Users.as_view(), name='back_account'),
    path('account/add-user', UserCreate.as_view(), name='add_user'),
    path('account/<str:username>/reset-pw', UserResetPw.as_view(), name='reset_user_pw'),
    path('account/<int:pk>/update', UserUpdate.as_view(), name='updat_user'),
    path('account/<int:pk>/delete', UserDelete.as_view(), name='delete_user'),
    path('group/',Groups.as_view(), name='back_group'),
    path('group/create', GroupCreate.as_view(), name='creat_gp'),
    path('group/<int:pk>/update', GroupUpadte.as_view(), name='update_group'),
    path('group/<int:pk>/delete', GroupDelete.as_view(), name='delete_group'),
    
]