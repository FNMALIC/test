from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm

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

def login_page(request):
    # return render(request,"")
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users_pages/profile.html')
    else:
        form = UserForm()
    return render(request, 'users_pages/login.html', {'form': form})