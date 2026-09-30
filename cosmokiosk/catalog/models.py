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
    checked_out = models.BooleanField(default=False)
    
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
    q1 = models.IntegerField(verbose_name="Overall_Rating")
    q2 = models.IntegerField(verbose_name="Service_Rating")
    q3 = models.IntegerField(verbose_name="Preparation_Rating")
    q4 = models.IntegerField(verbose_name="Professional_Rating")
    q5 = models.IntegerField(verbose_name="Warmth_Rating")
    q6 = models.IntegerField(verbose_name="Attitude_Rating")
    q7 = models.IntegerField(verbose_name="Consultant_Rating")
    q8 = models.IntegerField(verbose_name="Experience_Rating")
    feedback_message = models.TextField(blank=True, null=True)
    
    client_info = models.ForeignKey('Client_Waiver', on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f"{self.client_info}"
    
class Waxing_Waiver(models.Model):
    medicine = models.BooleanField(
        verbose_name="Medicine",
        null=True
    )

    allergy = models.BooleanField(
        verbose_name="Bee Allergy",
        null=True
    )

    soap_use = models.BooleanField(
        verbose_name="Skin Care Use",
        null=True
    )

    exposed = models.BooleanField(
        verbose_name="Light Exposure",
        null=True
    )

    health_issues = models.BooleanField(
        verbose_name="Health Conditions",
        null=True
    )
    agreement = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.agreement


class Services(models.Model):

    perm = models.BooleanField(verbose_name="perm", default=False )
    color = models.BooleanField(verbose_name="color", default=False )
    hairstyle = models.BooleanField(verbose_name="hairstyle", default=False )
    waxing = models.BooleanField(verbose_name="waxing", default=False)
    nails = models.BooleanField(verbose_name="nails", default=False)
    client_info = models.OneToOneField(
        Client_Waiver, 
        on_delete=models.CASCADE, 
        primary_key=True)
    
    
    def __str__(self):
        return f"{self.client_info}" 
    

