from django.shortcuts import render
from django.views import View

from database.operations import authenticate, check_if_exists, execute_insert_query
from user.forms import UserLoginForm, UserRegistrationForm
from django.shortcuts import redirect

from user.models import User
from django.contrib.auth.views import LoginView
from pydantic import ValidationError
# Create your views here.

class UserRegistrationView_(View):
    form_class = UserRegistrationForm
    def get(self,request,*args,**kwargs):
        context = {}
        context["form"] = UserRegistrationForm()
        return render(request,"user/register.html",context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print("form is valid")
            userdata = {}
            full_name = form.cleaned_data["full_name"]
            email = form.cleaned_data.get("email")
            address = form.cleaned_data.get("address")
            phone = form.cleaned_data.get("phone")
            gender = form.cleaned_data.get("gender")
            query  = 'INSERT INTO "User" (full_name,email,address,phone,gender) VALUES (%s,%s,%s,%s,%s) '
            values = (full_name,email,address,phone,gender)
            execute_insert_query(query,values)
            return redirect("/")
        

class UserRegistrationView(View):
    form_class = UserRegistrationForm
    def get(self,request,*args,**kwargs):
        context = {}
        context["form"] = UserRegistrationForm()
        return render(request,"user/register.html",context)
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            print("form is valid")
            try:
                user = User(**form.cleaned_data)
                print(user)
                print(user.model_dump())
            except ValidationError as e:
                print(str(e))
            query  = user.get_insert_query()
            values = user.get_values()
            execute_insert_query(query,values)
            return redirect("/")
        else:
            context = {}
            context["form"] =form
            return render(request,"user/register.html",context)
        
class UserLoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user:
            return redirect("index")
            
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,*args,**kwargs):
        context = {}
        context["form"] = UserLoginForm()
        print(request.user)
        return render(request,"user/login.html",context)
    
    def post(self,request,*args,**kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email,password)
            if user:
                request.session["user_email"] = user.email
                return redirect("index")
                
            else:
                print("not authenticated...")

            context = {}
            context["form"] = form
            return render(request,"user/login.html",context)
                


class UserLogoutView(View):
    def get(self,request,*args,**kwargs):
        if 'user_email' in request.session:
            del request.session['user_email']
        return redirect("user_login")
