from django.urls import path
from app.views import *

urlpatterns = [
    path('',index,name='index'),

    # Host city urls
    path('en/bordeaux',bordeaux_page,name='bordeaux'),
    path('en/lille_metropole',lille_metropole_page,name='lille_metropole'),
    path('en/lyon',lyon_page,name='lyon'),
    path('en/marseille',marseille_page,name='marseille'),
    path('en/nantes',nantes_page,name='nantes'),
    path('en/nice',nice_page,name='nice'),
    path('en/saint_denis',saint_denis_page,name='saint_denis'),
    path('en/saint_etienne',saint_etienne_page,name='saint_etienne'),
    path('en/toulouse',toulouse_page,name='toulouse'),

    # Qualified team page
    path('en/argentina',argentina_page,name='argentina'),  
    path('en/australia',australia_page,name='australia'),  
    path('en/chile',chile_page,name='chile'),  
    path('en/england',england_page,name='england'),  
    path('en/fiji',fiji_page,name='fiji'),  
    path('en/teamfrance',teamfrance_page,name='teamfrance'),  
    path('en/georgia',georgia_page,name='georgia'),  
    path('en/ireland',ireland_page,name='ireland'),  
    path('en/Italy',Italy_page,name='Italy'),  
    path('en/japan',japan_page,name='japan'),  
    path('en/namibia',namibia_page,name='namibia'),  
    path('en/new_zealand',new_zealand_page,name='new_zealand'),  
    path('en/portugal',portugal_page,name='portugal'),  
    path('en/romania',romania_page,name='romania'),  
    path('en/samoa',samoa_page,name='samoa'),  
    path('en/south_africa',south_africa_page,name='south_africa'),  
    path('en/scotland',scotland_page,name='scotland'),  
    path('en/tonga',tonga_page,name='tonga'),  
    path('en/uruguay',tonga_page,name='uruguay'),  
    path('en/wales',wales_page,name='wales'),  


    # others
    path('en/contact',contact_page,name='wales'),  
    path('en/parking_booking',parking_booking_page,name='parking_book'),  
    path('en/accessibility_booking',accessibility_booking_page,name='accessibility_booking'),  
    path('en/faq',faq_page,name='faq'),  


    # users
    path('register',login_page,name='register'),  
    path('profile',edit_profile,name='profile'), 
    path('logout/', logout_view, name='logout'), 

    path('dashboard/',dashboard_page,name='dashboard'),  
    path('orders/',order_page,name='orders'),  
    path('notification/',notification_page,name='notification'),  
    path('payments/',payment_page,name='payments'),  
    path('resales/',resales_page,name='resales'),  
    path('document/',document_page,name='documents'),  
    # path('profile',edit_profile,name='profile'),  

] 
