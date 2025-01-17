from django.views import View
from base.mixins import get_redirected
from user.db_utils import authenticate
from user.forms import UserLoginForm, UserRegistrationForm   
from django.shortcuts import render,redirect
from django.contrib import messages

from user.models import User

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
            form.cleaned_data["user_type"] = "admin"
            User.create(**form.cleaned_data)
         
            messages.success(request,"Registration Complete.")
            return redirect("user_login")
        else:
            context = {}
            context["form"] =form
            return render(request,"user/register.html",context)
        
class UserLoginView(View):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user:
            return get_redirected(self.request.user)
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        context = {}
        context["form"] = UserLoginForm()
        return render(request,"registration/login.html",context)
    
    def post(self,request,*args,**kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email,password)
            if user:
                request.session["user_email"] = user.email
                messages.success(request,"login Successful")
                return get_redirected(user)
                

                
            else:
                messages.error(request,"Invalid Credentials.Please try again.")
        context = {}
        context["form"] = form
        return render(request,"registration/login.html",context)
                


class UserLogoutView(View):
    def get(self,request,*args,**kwargs):
        if 'user_email' in request.session:
            del request.session['user_email']
        messages.success(request,"You have been logged out.Please Log in again to continue.")
        return redirect("user_login")
