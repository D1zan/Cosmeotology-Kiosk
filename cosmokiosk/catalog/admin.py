from django.contrib import admin
from .models import Profile_Instance, Client_Waiver, Feedback_Questions, Feedback, Waxing_Waiver, Services


class Profile_Instance_Admin(admin.ModelAdmin): #For the Profile_Instance model
    list_display = ("username", "email_address", "first_name", "last_name", "is_student", "is_shop_instructor")
    list_per_page = 25

class ClientAdmin(admin.ModelAdmin): # For the Client_Waiver model
    list_display = ("id","first_name", "last_name", "date_time")
    list_per_page = 25

class QuestionAdmin(admin.ModelAdmin): # For the Feedback_Questions model
    list_display = ("question", "question_text") 
    list_per_page = 25

class ResponsesAdmin(admin.ModelAdmin): # For the Feedback model
    list_display = ("client_info", "q1","q2","q3","q4","q5","q6","q7","q8", "feedback_message")
    
    list_per_page = 25

class WaxingAdmin(admin.ModelAdmin): # For the Waxing_Waiver model
    list_display = ("medicine","allergy","soap_use","exposed","health_issues","agreement")
    list_per_page = 25

class ServiceAdmin(admin.ModelAdmin): # For the Services model
    list_display = ("client_info", "perm", "color", "hairstyle", "waxing", "nails")
    list_per_page = 25
    
    
models_and_admins = [
     (Profile_Instance, Profile_Instance_Admin),
     (Client_Waiver, ClientAdmin),
     (Feedback_Questions, QuestionAdmin),
     (Feedback, ResponsesAdmin),
     (Waxing_Waiver, WaxingAdmin),
     (Services, ServiceAdmin),
]

for model, admins in models_and_admins:
         admin.site.register(model, admins)
