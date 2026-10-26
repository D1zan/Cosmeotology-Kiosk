
from django.contrib import admin
from django import forms

from .models import (
    Profile_Instance,
    Client_Waiver,
    Feedback_Questions,
    Feedback,
    Waxing_Waiver,
    Services,
)


# Form used to securely set teacher passwords
class ProfileInstanceAdminForm(forms.ModelForm):
    new_password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label="Set New Password",
        help_text="Leave blank to keep the existing password."
    )

    class Meta:
        model = Profile_Instance
        exclude = ["password"]

    def save(self, commit=True):
        instance = super().save(commit=False)

        new_password = self.cleaned_data.get("new_password")

        if new_password:
            instance.set_password(new_password)

        if commit:
            instance.save()
            self.save_m2m()

        return instance


# Admin settings for teacher profiles
class ProfileInstanceAdmin(admin.ModelAdmin):
    form = ProfileInstanceAdminForm

    list_display = (
        "first_name",
        "last_name",
        "email_address",
        "password_status",
        "is_student",
        "is_shop_instructor",
    )

    list_per_page = 25

    @admin.display(description="Password")
    def password_status(self, obj):
        if obj.password and obj.password.startswith(
            ("pbkdf2_", "argon2", "bcrypt", "scrypt")
        ):
            return "Password Set"
        return "Not Set"

# Admin settings for client waivers
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "date_time",
    )
    list_per_page = 25


# Admin settings for feedback questions
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question", "question_text")
    list_per_page = 25


# Admin settings for feedback responses
class ResponsesAdmin(admin.ModelAdmin):
    list_display = (
        "client_info",
        "q1", "q2", "q3", "q4",
        "q5", "q6", "q7", "q8",
        "feedback_message",
    )
    list_per_page = 25


# Admin settings for waxing waivers
class WaxingAdmin(admin.ModelAdmin):
    list_display = (
        "medicine",
        "allergy",
        "soap_use",
        "exposed",
        "health_issues",
        "agreement",
    )
    list_per_page = 25


# Admin settings for services
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "client_info",
        "perm",
        "color",
        "hairstyle",
        "waxing",
        "nails",
    )
    list_per_page = 25


# Register each model exactly once
admin.site.register(Profile_Instance, ProfileInstanceAdmin)
admin.site.register(Client_Waiver, ClientAdmin)
admin.site.register(Feedback_Questions, QuestionAdmin)
admin.site.register(Feedback, ResponsesAdmin)
admin.site.register(Waxing_Waiver, WaxingAdmin)
admin.site.register(Services, ServiceAdmin)
