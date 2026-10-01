from django.shortcuts import render, redirect
from .forms import ClientWaiverForm, FeedbackForm, WaxingWaiverForm, ServicesForm
from .models import Client_Waiver, Services, Waxing_Waiver
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

def client_waiver_view(request):
    return signin_view(request)

def welcome_page(request):
    return render(request, 'catalog/welcome.html')
    
def services_page(request):
    if request.method == "POST":
        form = ServicesForm(request.POST)

        if form.is_valid():
            client_id = request.session.get('client_id')

            if client_id:
                client = Client_Waiver.objects.get(id=client_id)

                # Save the client's selected services FIRST
                service = form.save(commit=False)
                service.client_info = client
                service.save()

                # If they selected waxing, send them to the waxing waiver
                if service.waxing:
                    return redirect('waxing_waiver')

                # If they did NOT select waxing
                return redirect('welcome')

        else:
            print("SERVICE FORM INVALID")
            print(form.errors)

    else:
        form = ServicesForm()

    return render(
        request,
        'catalog/services.html',
        {'form': form}
    )


#this is the place for all the forms stuff
def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)

            
            client_id = request.session.get('checkout_client_id')

            if client_id:
                try:
                    client = Client_Waiver.objects.get(id=client_id)

                    feedback.client_info = client
                    feedback.save()

                    
                    client.checked_out = True
                    client.save()

                except Client_Waiver.DoesNotExist:
                    
                    feedback.save()

            else:
                
                feedback.save()

           
            request.session.pop('checkout_client_id', None)

           
            return redirect('welcome')

        else:
            print("FEEDBACK FORM INVALID")
            print(form.errors)

    else:
        form = FeedbackForm()

    return render(
        request,
        'catalog/feedback.html',
        {'form': form}
    )

def waiver_view(request):
    if request.method == "POST":
        print("USER SUBMITTED")
        form = WaxingWaiverForm(request.POST)

        if form.is_valid():
            print("VALID")

            waiver = form.save(commit=False)

            client_id = request.session.get('client_id')

            if client_id:
                try:
                    waiver.client_info = Client_Waiver.objects.get(
                        id=client_id
                    )
                except Client_Waiver.DoesNotExist:
                    pass

            waiver.save()

            return redirect('welcome')

        else:
            print("INVALID", form.errors)

    else:
        form = WaxingWaiverForm()

    full_name = request.session.get('saved_full_name', '')

    return render(
        request,
        'catalog/waxing.html',
        {
            'form': form,
            'full_name': full_name
        }
    )



def checkout(request):

    clients = Client_Waiver.objects.filter(checked_out=False).order_by('first_name', 'last_name')

    if request.method == "POST":
        selected_client_id = request.POST.get("client_id")

        if selected_client_id:
            request.session["checkout_client_id"] = selected_client_id
            return redirect("feedback")

    return render(
        request,
        "catalog/checkout.html",
        {"clients": clients}
    )


def teacher_dashboard(request): # gets all clients who have not checked out
    clients = Client_Waiver.objects.filter(
        checked_out=False
    ).order_by('date_time') # puts in order by date and time

    return render(
        request,
        'catalog/teacher-dashboard.html', # sends to the teachers dashboard
        {'clients': clients}
    )

def client_details(request, client_id):
    try:
        client = Client_Waiver.objects.get(id=client_id)
    except Client_Waiver.DoesNotExist:
        return redirect('teacher_dashboard')

    try:
        services = Services.objects.get(client_info=client)
    except Services.DoesNotExist:
        services = None

    try:
        waxing_waiver = Waxing_Waiver.objects.get(client_info=client)
    except Waxing_Waiver.DoesNotExist:
        waxing_waiver = None

    return render(
        request,
        'catalog/client-details.html',
        {
            'client': client,
            'services': services,
            'waxing_waiver': waxing_waiver
        }
    )

def teacher_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")

        # Make sure both fields were filled out
        if full_name and email:

            # Split full name into first and last name
            name_parts = full_name.strip().split(" ", 1)

            first_name = name_parts[0]

            if len(name_parts) > 1:
                last_name = name_parts[1]
            else:
                last_name = ""

            # Check if this email already belongs to a user
            user = User.objects.filter(email=email).first()

            # If they don't exist, create them
            if not user:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )

                # They don't have a password yet
                user.set_unusable_password()
                user.save()

            return redirect("welcome")

    return render(request, "catalog/teacher_sign_in.html")