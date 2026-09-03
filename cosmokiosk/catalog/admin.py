from django.contrib import admin
#from django.contrib.admin import ModelAdmin
#from django.apps import apps
from .models import Client_Waiver, Feedback_Questions, Feedback, Waxing_Waiver, Services


class ClientAdmin(admin.ModelAdmin): # For the Client_Waiver model
    list_display = ("first_name", "last_name", "date_time")
    list_per_page = 25

class QuestionAdmin(admin.ModelAdmin): # For the Feedback_Questions model
    list_display = ("question", "question_text") 
    list_per_page = 25

class ResponsesAdmin(admin.ModelAdmin): # For the Feedback model
    list_display = ("q1","q2","q3","q4","q5","q6","q7","q8","client_info")
    list_per_page = 25

class WaxingAdmin(admin.ModelAdmin): # For the Waxing_Waiver model
    list_display = ("medicine","allergy","soap_use","exposed","health_issues","agreement","client_info")
    list_per_page = 25

class ServiceAdmin(admin.ModelAdmin): # For the Services model
    list_display = ("perm", "color", "hairstyle", "waxing", "nails", "client_info")
    list_per_page = 25
models_and_admins = [
     (Client_Waiver, ClientAdmin),
     (Feedback_Questions, QuestionAdmin),
     (Feedback, ResponsesAdmin),
     (Waxing_Waiver, WaxingAdmin),
     (Services, ServiceAdmin),
]

for model, admins in models_and_admins:
         admin.site.register(model, admins)

# admin.site.register(Client_Waiver, ClientAdmin)
# admin.site.register(Feedback_Questions, QuestionAdmin) #delete after testing



# models_and_admins = {
#     (Client_Waiver, ClientAdmin)
# }

# for model, admin in models_and_admins:
#         admin.site.register(model, admin)

# app_models = apps.get_app_config('catalog').get_models()
# admin_models = [ClientAdmin, QuestionAdmin, ResponsesAdmin, WaxingAdmin, ServiceAdmin]
# for m in app_models:
#     #for j in admin_models:
#         admin.site.register(m)
     
# #for j in app_models: