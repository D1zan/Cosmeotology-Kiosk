from django import forms
from .models import Client_Waiver, Waxing_Waiver, Feedback_Questions, Feedback, Services
from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone




class ClientWaiverForm(forms.ModelForm):

    
    consent = forms.BooleanField(
        required=True,
        error_messages={'required': 'You must accept the Terms of Service please check the box to agree.'}
        )

    class Meta:
        model = Client_Waiver
        fields = ['first_name', 'last_name']

    # Function handles id_first_name input field on the Sign-In HTML page.
    # If the field is filled, then extra spaces will be stripped and the name will be saved. 
    # A validation error will be raised if it is submitted empty.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if not first_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in first_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('First name can only contain letters.')
            
        return first_name
    
    # Function handles id_last_name input field on the Sign-In HTML page.
    # If the field is filled, then extra spaces will be stripped and the name will be saved. 
    # A validation error will be raised if it is submitted empty.
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if not last_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in last_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('Last name can only contain letters.')
            
        return last_name
    
from django import forms
from .models import Waxing_Waiver


class WaxingWaiverForm(forms.ModelForm):

    YES_NO_CHOICES = [
        (True, "Yes"),
        (False, "No"),
    ]

    medicine = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        coerce=lambda x: x == "True",
        required=True,
        error_messages={
            "required": "Please answer this question."
        }
    )

    allergy = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        coerce=lambda x: x == "True",
        required=True,
        error_messages={
            "required": "Please answer this question."
        }
    )

    soap_use = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        coerce=lambda x: x == "True",
        required=True,
        error_messages={
            "required": "Please answer this question."
        }
    )

    exposed = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        coerce=lambda x: x == "True",
        required=True,
        error_messages={
            "required": "Please answer this question."
        }
    )

    health_issues = forms.TypedChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        coerce=lambda x: x == "True",
        required=True,
        error_messages={
            "required": "Please answer this question."
        }
    )

    agreement = forms.CharField(
        required=True,
        error_messages={
            "required": "Please sign before submitting."
        }
    )

    class Meta:
        model = Waxing_Waiver
        fields = [
            "medicine",
            "allergy",
            "soap_use",
            "exposed",
            "health_issues",
            "agreement",
        ]


    # write code so that the user name == the name they use in agreement
    # use the super() method. what that does is grabs the original method for that class and uses it on the 
    # method used that we coded.


class FeedbackQuestionsForm(forms.ModelForm):

    question_text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'optional feedback'})
    )

    class Meta:
        model = Feedback_Questions
        fields = ['question', 'question_text']
        widgets = {
            'question': forms.RadioSelect(),
        }


class FeedbackForm(forms.ModelForm):
    class Meta: 
        model = Feedback
        fields = ['q1','q2','q3','q4','q5','q6','q7','q8', 'feedback_message']

        def clean(self):
            cleaned_data = super().clean()
            return cleaned_data 
    



class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['perm', 'color', 'hairstyle', 'waxing', 'nails']

    def clean(self):
        cleaned_data = super().clean()
        fields = ['perm', 'color', 'hairstyle', 'waxing', 'nails'] 
        return cleaned_data  

