from django.shortcuts import render
from django.views import View

from base.mixins import HasPermissionMixin
from base.utils import DeleteMixin, PartialTemplateMixin
from base.views import BaseUpdateView
from music.models import Artist
from user.forms import ArtistCreateForm, UserCreationForm, UserRegistrationForm, UserUpdateForm
from django.shortcuts import redirect

from user.models import User
from django.urls import reverse_lazy
from typing import Any  
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.


class UserMixin(HasPermissionMixin,PartialTemplateMixin):
    form_class = UserRegistrationForm
    model = User
    success_url = reverse_lazy("user_list")
    template_dir="user/"
    authorized_groups = ["admin"]

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
    
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = self.model.create(**form.cleaned_data)

            if user.user_type == "artist":
                Artist.create(user_id=user.id,first_album_release_year=form.cleaned_data.get("first_album_release_year"))
            messages.success(request,"User Created.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.form_class()
        return context
        
class UserUpdateView(UserMixin,BaseUpdateView):
    form_class = UserUpdateForm
    template_name = "update.html"
    authorized_groups = ["admin","artist_manager"]

    def post(self,request,*args,**kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST,email=instance.email)
        if form.is_valid():      
            instance.update(**form.cleaned_data)
            messages.success(request,"User Updated.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
class UserDeleteView(UserMixin,DeleteMixin,View):
    authorized_groups = ["admin","artist_manager"]



# Artist
class ArtistListView(UserMixin,ListView):
    template_name = "artist_user/artist_user_list.html"
    template_dir="artist_user/"
    success_url = "artist_list"
    paginate_by = 10
    authorized_groups = ["admin","artist_manager"]

    def get_queryset(self):
        return self.get_artist_list_queryset(self.request)
    
    @staticmethod
    def get_artist_list_queryset(request):
        search = request.GET.get("q")
        filter_args = {"user_type":"artist"}
        if search:
            filter_args["full_name__icontains"] = f"%{search}%"
        
        if request.user.user_type == "artist_manager":
            return User.manager_filter(manager_user_id=request.user.id,**filter_args)
        

        return User.filter_from_db(**filter_args)      
    

class ArtistUserCreateView(UserCreateView):
    form_class = ArtistCreateForm
    success_url = reverse_lazy("artist_list")
    authorized_groups = ["admin","artist_manager"]
    
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
            if request.user.user_type == "artist_manager":
                artist_manager_id = self.request.user.id
            else:
                artist_manager_id = None
            Artist.create(user_id=user.id,
                          artist_manager_id = artist_manager_id,
                          first_album_release_year=form.cleaned_data.get("first_album_release_year"))
            messages.success(request,"Artist Created.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})

