from django.shortcuts import render, redirect
from .forms import Waxing_Waiver, ClientWaiverForm, Feedback_Questions, FeedbackForm, WaxingWaiverForm, ServicesForm, Client_Waiver
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request, 'catalog/welcome.html') 


def signin_view(request):
    if request.method == "POST":
        form = ClientWaiverForm(request.POST)
        if form.is_valid():
            client_waiver = form.save(commit=False)
            client_waiver.date_time = timezone.now()
            client_waiver.save()
            print("--- DATA SUCCESSFULLY SAVED TO DATABASE ---")
            first_name = form.cleaned_data.get('first_name', '')
            last_name = form.cleaned_data.get('last_name', '')
            request.session['client_id'] = client_waiver.id
            request.session['saved_full_name'] = f"{first_name} {last_name}".strip()
            return redirect('services')
        else: 
            print("--- FORM VALIDATION FAILED ---")
            print(form.errors.as_data())
    else:
        form = ClientWaiverForm(initial={'date_time': timezone.now()})
    return render(request, 'catalog/sign-in.html', {'form': form})


def welcome_page(request):
    return render(request, 'catalog/welcome.html')
    
def services_page(request):
    if request.method == "POST":
        print("SERVICE SUBMITTED")
        form = ServicesForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            client_id = request.session.get('client_id')
            if client_id:
                try:
                    service.client_info = Client_Waiver.objects.get(id=client_id)
                except Client_Waiver.DoesNotExist:
                    print("--- WARNING: CLIENT_ID NOT FOUND IN YOUR MOM ---")

            service.save()    
            return redirect('welcome')
        else:
            print("services is not valid dorks")
    else:
        form = ServicesForm()
    
    return render(request, 'catalog/services.html', {'form': form})


#this is the place for all the forms stuff

def waiver_view(request):
    if request.method == "POST":
        print("USER SUBMITTED")
        form = WaxingWaiverForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            return redirect('welcome')
        else:
            print("INVALID", form.errors)
    else:
        form = WaxingWaiverForm()

    full_name = request.session.get('saved_full_name', '')
    return render(request, 'catalog/waxing.html', {'form':form, 'full_name':full_name})


def client_waiver_view(request):
    return signin_view(request)


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            client_id = request.session.get('client_id')
            if client_id:
                try:
                    feedback.client_info = Client_Waiver.objects.get(id=client_id)
                except Client_Waiver.DoesNotExist:
                    pass
            feedback.save()
            return redirect('welcome')  
        else:
            print(form.errors)
    else:
        form = FeedbackForm()
    return render(request, 'catalog/feedback.html', {'form': form})
   
