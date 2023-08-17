from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.http import HttpResponse
from .forms import UserForm, UserProfileForm

# Create your views here.

def index(request):
    return render(request,'visiter/home.html')


# Host city
def bordeaux_page(request):
    return render(request,'visiter/host_city_pages/bordeaux.html')

def lille_metropole_page(request):
    return render(request,'visiter/host_city_pages/lille_metropole.html') 

def lyon_page(request):
    return render(request,'visiter/host_city_pages/lyon.html') 

def marseille_page(request):
    return render(request,'visiter/host_city_pages/marseille.html') 

def nantes_page(request):
    return render(request,'visiter/host_city_pages/nantes.html') 

def nice_page(request):
    return render(request,'visiter/host_city_pages/nice.html') 

def saint_denis_page(request):
    return render(request,'visiter/host_city_pages/saint_denis.html') 

def saint_etienne_page(request):
    return render(request,'visiter/host_city_pages/saint_etienne.html') 

def toulouse_page(request):
    return render(request,'visiter/host_city_pages/toulouse.html') 


# Qualified city 

def argentina_page(request):
    return render(request,'visiter/qualified_team_pages/argentina.html')

def australia_page(request):
    return render(request,'visiter/qualified_team_pages/australia.html')

def chile_page(request):
    return render(request,'visiter/qualified_team_pages/chile.html')

def england_page(request):
    return render(request,'visiter/qualified_team_pages/england.html')

def fiji_page(request):
    return render(request,'visiter/qualified_team_pages/fiji.html')

def teamfrance_page(request):
    return render(request,'visiter/qualified_team_pages/teamfrance.html')

def georgia_page(request):
    return render(request,'visiter/qualified_team_pages/georgia.html')

def ireland_page(request):
    return render(request,'visiter/qualified_team_pages/ireland.html')

def Italy_page(request):
    return render(request,'visiter/qualified_team_pages/Italy.html')

def japan_page(request):
    return render(request,'visiter/qualified_team_pages/japan.html')

def namibia_page(request):
    return render(request,'visiter/qualified_team_pages/namibia.html')

def new_zealand_page(request):
    return render(request,'visiter/qualified_team_pages/new_zealand.html')

def portugal_page(request):
    return render(request,'visiter/qualified_team_pages/portugal.html')

def romania_page(request):
    return render(request,'visiter/qualified_team_pages/romania.html')

def samoa_page(request):
    return render(request,'visiter/qualified_team_pages/samoa.html')

def south_africa_page(request):
    return render(request,'visiter/qualified_team_pages/south_africa.html')

def scotland_page(request):
    return render(request,'visiter/qualified_team_pages/scotland.html')

def tonga_page(request):
    return render(request,'visiter/qualified_team_pages/tonga.html')

def uruguay_page(request):
    return render(request,'visiter/qualified_team_pages/uruguay.html')

def wales_page(request):
    return render(request,'visiter/qualified_team_pages/wales.html')



# others

def contact_page(request):
    return render(request,'visiter/contact.html')

def parking_booking_page(request):
    return render(request,'visiter/parking.html')

def accessibility_booking_page(request):
    return render(request,'visiter/accessibility.html')

def faq_page(request):
    return render(request,'visiter/faq.html')

# @login_required
def dashboard_page(request):
    return render(request,'users_pages/dashboard.html')

def order_page(request):
    return render(request,'users_pages/orders.html')


def notification_page(request):
    print(request.path)
    return render(request,'users_pages/notification.html')


def payment_page(request):
    return render(request,'users_pages/payment.html')


def resales_page(request):
    return render(request,'users_pages/resales.html')


def document_page(request):
    return render(request,'users_pages/document.html')

def login_page(request):
    # return render(request,"")
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password_user'])
            user.save()
            auth_user = authenticate(request, email=user.email, password=form.cleaned_data['password_user'])
            if auth_user is not None:
                login(request, auth_user)
                return redirect('/profile')
    else:
        form = UserForm()
    return render(request, 'users_pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login_url')

def edit_profile(request):
    print(request.path)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        # print(form.cleaned_data['first_name'])
        print(request.POST)
        if form.is_valid():
            # Update the user instance with the form data
            user.first_name = form.cleaned_data['first_name']
            # print(user.first_name)
            user.last_name = form.cleaned_data['last_name']
            user.date_birth = form.cleaned_data['date_of_birth']
            user.mobile_phone = form.cleaned_data['mobile_phone']
            user.street_address = form.cleaned_data['street_address']
            user.postal_code = form.cleaned_data['postal_code']
            user.city = form.cleaned_data['city']
            user.country = form.cleaned_data['country']
            user.Favourite_national_team = form.cleaned_data['favourite_national_team']
            user.Favourite_city = form.cleaned_data['favourite_city']
            user.favourite_language = form.cleaned_data['favourite_language']
            user.club_coeur = form.cleaned_data['club_de_coeur']
            print()
            try:
                user.save()
                return redirect('/dashboard')
            except Exception as e:
                print(e)
            # if user.save():
                
            # else:
            #     return redirect('/register')
        else:
            # Handle the case when the form is not valid 
            print(form.errors) 
    else:
        form = UserProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_of_birth': user.date_birth,
            'mobile_phone': user.mobile_phone,
            'street_address': user.street_address,
            'postal_code': user.postal_code,
            'city': user.city,
            'country': user.country,
            'favourite_national_team': user.Favourite_national_team,
            'favourite_city': user.Favourite_city,
            'favourite_language': user.favourite_language,
            'club_de_coeur': user.club_coeur,
        })
    return render(request, 'users_pages/profile.html', {'form': form})