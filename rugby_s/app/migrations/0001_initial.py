# Generated by Django 4.2.3 on 2023-08-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('date_birth', models.DateField(null=True)),
                ('mobile_phone', models.CharField(max_length=14, null=True)),
                ('street_address', models.CharField(max_length=50, null=True)),
                ('postal_code', models.CharField(max_length=45, null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('country', models.CharField(max_length=60, null=True)),
                ('Favourite_national_team', models.CharField(max_length=50, null=True)),
                ('Favourite_city', models.CharField(max_length=60, null=True)),
                ('favourite_language', models.CharField(max_length=60, null=True)),
                ('club_coeur', models.CharField(max_length=60, null=True)),
                ('sexe_user', models.CharField(max_length=50, null=True)),
                ('email_user', models.CharField(max_length=50, null=True)),
                ('password_user', models.CharField(max_length=90, null=True)),
                ('card_number', models.CharField(max_length=35, null=True)),
                ('exp_date', models.CharField(max_length=35, null=True)),
                ('CVV', models.CharField(max_length=4, null=True)),
                ('account_name', models.CharField(max_length=53, null=True)),
                ('owner_name', models.CharField(max_length=50, null=True)),
                ('IBAN_accountNumber', models.CharField(max_length=50, null=True)),
                ('BIC_SWIFT', models.CharField(max_length=60, null=True)),
                ('address_gmail', models.CharField(max_length=95, null=True)),
                ('password_gmail', models.CharField(max_length=95, null=True)),
            ],
        ),
    ]
