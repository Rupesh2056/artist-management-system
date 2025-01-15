from django.shortcuts import render
from django.views import View

from base.mixins import HasPermissionMixin
from base.utils import DeleteMixin, PartialTemplateMixin
from base.views import BaseUpdateView
from database.operations import  execute_db_query, execute_insert_query, execute_select_query
from user.db_utils import authenticate
from user.forms import UserCreationForm, UserLoginForm, UserRegistrationForm, UserUpdateForn
from django.shortcuts import redirect

from user.models import User
from django.contrib.auth.views import LoginView
from pydantic import ValidationError
from django.urls import reverse_lazy
from typing import Any  
from django.views.generic import ListView

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
                user = User.create(**form.cleaned_data)
            except ValidationError as e:
                print(str(e))
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
        return render(request,"registration/login.html",context)
    
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



class UserMixin(HasPermissionMixin,PartialTemplateMixin):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy("user_list")
    queryset = User.filter_from_db()
    template_dir="user/"
    authorized_goups = ["admin"]

class UserListView(UserMixin,ListView):
    template_name = "user/user_list.html"
    success_url = "user_list"
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get("q")
        filter_args = {}
        if search:
            filter_args["full_name__icontains"] = f"%{search}%"

        return User.filter_from_db(**filter_args)

class UserCreateView(UserMixin,View):
    form_class = UserCreationForm
    template_name = "create.html"
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)   
        return render(request,self.get_template_names(),context)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.form_class()
        return context
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.model.create(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
        
class UserUpdateView(UserMixin,BaseUpdateView):
    form_class = UserUpdateForn
    template_name = "update.html"

    def post(self,request,*args,**kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST,email=instance.email)
        if form.is_valid():      
            instance.update(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
class UserDeleteView(UserMixin,DeleteMixin,View):
    ...

