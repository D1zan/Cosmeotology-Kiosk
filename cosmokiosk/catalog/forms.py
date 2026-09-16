from django import forms
from .models import Client_Waiver, Waxing_Waiver, Feedback_Questions, Feedback, Services
from django.core.exceptions import ValidationError
import datetime
from django.utils.translation import gettext_lazy as _
from django.utils import timezone



class ClientWaiverForm(forms.ModelForm):

    consent = forms.BooleanField(
        required=True,
        error_messages={'required': 'You must accept the Terms of Service please check the box to agree.'})

    class Meta:
        model = Client_Waiver
        fields = ['first_name', 'last_name']

    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if not first_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in first_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('First name can only contain letters.')
            
        return first_name
    
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if not last_name:
            raise ValidationError('Name fields cannot be empty.')
        
        for char in last_name:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError('Last name can only contain letters.')
            
        return last_name
    
    
    
class WaxingWaiverForm(forms.ModelForm):
    class Meta:
        model = Waxing_Waiver
        fields = ['medicine', 'allergy', 'soap_use', 'exposed', 'health_issues', 'agreement']
    # def clean(self):
    #     cleaned_data = super().clean()
    #     boolean_fields = ['medicine', 'allergy', 'soap_use', 'exposed', 'health_issues', 'agreement'] 
    #     return cleaned_data   


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
        fields = ['q1','q2','q3','q4','q5','q6','q7','q8'] #,'feedback_question'

        def clean(self):
            cleaned_data = super().clean()
            fields = ['q1','q2','q3','q4','q5','q6','q7','q8'] 
            return cleaned_data 
    


# bug testing comment  
class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['perm', 'color', 'hairstyle', 'waxing', 'nails', 'client_info']

    def clean(self):
        cleaned_data = super().clean()
        fields = ['perm', 'color', 'hairstyle', 'waxing', 'nails', 'client_info'] 
        return cleaned_data  

