from django.shortcuts import render
from django.views import View

from base.mixins import HasPermissionMixin
from base.utils import DeleteMixin, PartialTemplateMixin
from base.views import BaseUpdateView
from music.models import Artist
from user.db_utils import authenticate
from user.forms import ArtistCreateForm, UserCreationForm, UserLoginForm, UserRegistrationForm, UserUpdateForn
from django.shortcuts import redirect

from user.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from typing import Any  
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.
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
            user = User.create(**form.cleaned_data)
         
            messages.success(request,"Registration Complete.")
            return redirect("user_login")
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
                messages.success(request,"login Successful")
                if user.user_type == "admin":
                    return redirect("index")
                elif user.user_type == "arrtist_manager":
                    return redirect("artist_list")
                else:
                    return redirect("album_list")

                
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



class UserMixin(HasPermissionMixin,PartialTemplateMixin):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy("user_list")
    template_dir="user/"
    authorized_goups = ["admin"]

class UserListView(UserMixin,ListView):
    template_name = "user/user_list.html"
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get("q")
        filter_args = {}
        if search:
            filter_args["full_name__icontains"] = f"%{search}%"

        return User.filter_from_db(**filter_args)

class UserCreateView(UserMixin,View):
    form_class = UserCreationForm
    template_name = "user/create.html"
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)   
        return render(request,self.get_template_names(),context)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.form_class()
        context["artist_form"] = self.form_class()
        return context
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = self.model.create(**form.cleaned_data)

            if user.user_type == "artist":
                Artist.create(user_id=user.id,first_album_release_year=form.cleaned_data.get("first_album_release_year"))
            messages.success(request,"User Created.")
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
            messages.success(request,"User Updated.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
class UserDeleteView(UserMixin,DeleteMixin,View):
    ...


class ArtistListView(UserMixin,ListView):
    template_name = "artist_user/artist_user_list.html"
    success_url = "artist_list"
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get("q")
        filter_args = {"user_type":"artist"}
        if search:
            filter_args["full_name__icontains"] = f"%{search}%"

        return User.filter_from_db(**filter_args)
    

class ArtistUserCreateView(UserCreateView):
    form_class = ArtistCreateForm
    success_url = reverse_lazy("artist_list")
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.form_class()
        context["is_artist"] = True
        return context
    
    def post(self,request,*args,**kwargs): # use request url on usercreate and remove this
        form = self.form_class(request.POST)
        if form.is_valid():
            form.cleaned_data["user_type"] = "artist"
            user = self.model.create(**form.cleaned_data)
            Artist.create(user_id=user.id,first_album_release_year=form.cleaned_data.get("first_album_release_year"))
            messages.success(request,"Artist Created.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})

