from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback_view, name='feedback'),
    path('sign-in', views.signin_view, name='sign-in'),
    path('welcome', views.welcome_page, name='welcome'),
    path('services', views.services_page, name='services'),
    path('waiver', views.client_waiver_view, name='client_waiver'),
    path('waxing', views.waiver_view, name='waxing_waiver'),
    path('checkout/', views.checkout, name='checkout'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/client/<int:client_id>/', views.client_details, name='client_details'),
    path('teacher-page/', views.teacher_page, name='teacher-page')
    ]