from django import forms 
from base.utils import BaseForm
from django.core.exceptions import ValidationError

from database.operations import check_if_exists
from django.contrib.auth.hashers import make_password,check_password
from datetime import timezone,timedelta
from user.models import User, UserTypeEnum


class UserForm(BaseForm,forms.Form):
    GENDER_CHOICES = (
        ("m","Male"),
        ("f","Female"),
        ("o","Other"),
        )
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=30)
    address = forms.CharField(max_length=255,required=False)
    phone = forms.CharField(max_length=20,required=False)
    dob = forms.DateField(
        widget=forms.DateInput(format="%Y-%m-%d",
                               attrs={'type': 'date',
                                      },),
        help_text='Select a date',
        input_formats=["%Y-%m-%d"],
        required=False
      
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

class UserRegistrationForm(UserForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self):
        data = self.cleaned_data["password"]
        if len(data) < 5:
            raise ValidationError("Password Length Must be greater than 5!")
        hashed_password = make_password(data)
        return hashed_password
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        if password:
            confirm_password = self.cleaned_data["confirm_password"]
            if not check_password(confirm_password,password):
                raise ValidationError("Password Doesnt match!")
        # else:
        #     raise ValidationError("Password Length Must be greater than 5!")   
        return password
    

    def clean_email(self):
        exists_query = f'select exists (select 1 from {User.get_table_name()} where email = %s)'
        email = self.cleaned_data["email"]
        if check_if_exists(exists_query,(email,)):
            raise ValidationError("This Email is already Registered!")
        return email
    


class UserCreationForm(UserRegistrationForm):
    USER_TYPE_CHOICES = (
        ("admin","Admin"),
        ("artist_manager","Artist Manager"),
        ("artist","Artist"),
    )
    user_type = forms.ChoiceField(choices = USER_TYPE_CHOICES)
    first_album_release_year = forms.IntegerField(required=False)


class ArtistCreateForm(UserRegistrationForm):
    first_album_release_year = forms.IntegerField(required=False)


class UserUpdateForm(UserForm):
    def __init__(self, *args,email=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.email=email
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        if email != self.email:
            exists_query = f'select exists (select 1 from {User.get_table_name()} where email = %s)'

            if check_if_exists(exists_query,(email,)):
                raise ValidationError("This Email is already Registered!")
        return email
    

class UserLoginForm(BaseForm,forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


    

