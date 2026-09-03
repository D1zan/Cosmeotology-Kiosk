from django.db import models
from django.urls import reverse # used  in get_absolute_url to get the URL for a specified ID
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

from django.utils import timezone
import uuid

# Create your models here.

# Create your models here.

# class Checking(models.Model):
#     name = models.CharField(max_length=100)
#     check_in = models.DateTimeField(auto_now_add=True)
#     check_out = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.na

# model up for review, may not need it
# models WILL GO THROUGH CHANGES, THEY ARE NOT FINAL. REMOVE THIS COMMENT WHEN THIS STATEMENT IS UNTRUEx

class Client_Waiver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
    
    def get_absolute_url(self):
        return reverse('client-info', args=[str(self.id)])
    
    

class Feedback_Questions(models.Model):
    question = models.IntegerField(unique=True)
    question_text = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Question {self.question}: {self.question_text}"
    
class Feedback(models.Model):
    q1 = models.BooleanField(verbose_name="Question #1", default=False)
    q2 = models.BooleanField(verbose_name="Question #2", default=False)
    q3 = models.BooleanField(verbose_name="Question #3", default=False)
    q4 = models.BooleanField(verbose_name="Question #4", default=False)
    q5 = models.BooleanField(verbose_name="Question #5", default=False)
    q6 = models.BooleanField(verbose_name="Question #6", default=False)
    q7 = models.BooleanField(verbose_name="Question #7", default=False)
    q8 = models.BooleanField(verbose_name="Question #8", default=False)
    client_info = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f"{self.client_info}"
    
class Waxing_Waiver(models.Model):
    # Questions .
    # timestamp = models.DateTimeField(auto_now_add=True) <-- needs attention
    medicine = models.BooleanField(verbose_name="Medicine", default=False) #Field that handles the use of certain medicine
    allergy = models.BooleanField(verbose_name="Bee Allergy", default=False) #Field that handles client allergy to bees
    soap_use = models.BooleanField(verbose_name="Skin Care Use", default= False)
    exposed = models.BooleanField(verbose_name="Light Exposure", default=False)
    health_issues = models.BooleanField(verbose_name="Health Conditions", default=False)
    
    # Other
    agreement = models.CharField(max_length=100) #Client Signature
    client_info = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return f"{self.client_info}"


class Services(models.Model):

    perm = models.BooleanField(verbose_name="perm", default=False )
    color = models.BooleanField(verbose_name="color", default=False )
    hairstyle = models.BooleanField(verbose_name="hairstyle", default=False )
    waxing = models.BooleanField(verbose_name="waxing", default=False)
    nails = models.BooleanField(verbose_name="nails", default=False)
    client_info = models.ForeignKey(Client_Waiver, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.client_info}"
    

