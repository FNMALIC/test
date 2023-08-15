from django.db import models
from .AbstractModel import BaseUser

class User(BaseUser):
    username = models.CharField(max_length=150, unique=False)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_birth = models.DateField(null=True)
    mobile_phone = models.CharField(max_length=14, null=True)
    street_address = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=45, null=True)
    city = models.CharField(max_length=60, null=True)
    country = models.CharField(max_length=60, null=True)
    Favourite_national_team = models.CharField(max_length=50, null=True)
    Favourite_city = models.CharField(max_length=60, null=True)
    favourite_language = models.CharField(max_length=60, null=True)
    club_coeur = models.CharField(max_length=60, null=True)
    sexe_user = models.CharField(max_length=50, null=True)
    password_user = models.CharField(max_length=90, null=True)
    card_number = models.CharField(max_length=35, null=True)
    exp_date = models.CharField(max_length=35, null=True)
    CVV = models.CharField(max_length=4, null=True)
    account_name = models.CharField(max_length=53, null=True)
    owner_name = models.CharField(max_length=50, null=True)
    IBAN_accountNumber = models.CharField(max_length=50, null=True)
    BIC_SWIFT = models.CharField(max_length=60, null=True)
    address_gmail = models.CharField(max_length=95, null=True)
    password_gmail = models.CharField(max_length=95, null=True)

    USERNAME_FIELD = 'email'


    def __str__(self):
            return self.first_name
    
    class Meta:
        db_table = 'user' 