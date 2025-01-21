from django.shortcuts import render
from django.views import View
from base.mixins import HasPermissionMixin, LoginRequiredMixin, get_redirected
from base.utils import DeleteMixin, PartialTemplateMixin
from base.views import BaseUpdateView
from music.forms import AlbumCreateForm, ArtistAlbumCreateForm, MusicCreateForm
from music.models import Album, Artist, Music
from typing import Any

from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.contrib import messages
from django.http import Http404, JsonResponse

# Create your views here.

class IndexView(HasPermissionMixin,PartialTemplateMixin,View):
    template_name = "music/index.html"
    authorized_groups = ["admin"]

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user:
            return redirect("user_login")
        
        if request.user.user_type == "admin":
            return super().dispatch(request,*args,**kwargs)
        else:
            return get_redirected(request.user)
    
    
    def get(self,request,*args,**kwargs):
        context = {}
        return render(request,self.get_template_names(),context)
    



class AlbumMixin(HasPermissionMixin,PartialTemplateMixin):
    form_class = AlbumCreateForm
    artist_form_class = ArtistAlbumCreateForm
    model = Album
    success_url = reverse_lazy("album_list")
    template_dir="album/"
    authorized_groups = ["admin","artist"]
    

    # def get(self,request,*args,**kwargs):
    #     context = self.get_context_data(**kwargs)   
    #     return render(request,self.get_template_names(),context)
    
    def get_choices(self):
        artists = Artist.filter_from_db()
        choices = [(None,"Select Artist")]
        
        for artist in artists:
            choices.append((artist.id,artist.user.full_name))
        return choices
    
    def get_object(self):
        obj =  self.model.get_from_db(id=self.kwargs.get("pk"))
        if self.request.user.user_type == "artist" and  obj.artist_id != self.request.user.artist_profile.id:
            raise Http404("not found")
        return obj
    
    def get_form_class(self,**kwargs):
        if self.request.user.user_type == "artist":
            return ArtistAlbumCreateForm(**kwargs)
        return self.form_class(choices=self.get_choices(),**kwargs)




class AlbumListView(AlbumMixin,ListView):
    template_name = "album/album_list.html"
    paginate_by = 10
    authorized_groups = ["admin","artist_manager","artist"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["authorized_groups"] = ["admin","artist"]
        return context

    def get_queryset(self):
        search = self.request.GET.get("q")
        artist_id = self.request.GET.get("artist",None)
        

        filter_args = {}
        
        if self.request.user.user_type == "artist":
            filter_args["artist_id"] = self.request.user.artist_profile.id

        elif artist_id:
            filter_args["artist_id"] = int(artist_id)


        if search:
            filter_args["title__icontains"] = f"%{search}%"

        if self.request.user.user_type == "artist_manager":
            return Album.manager_filter(manager_user_id=self.request.user.id,**filter_args)

        return Album.filter_from_db(**filter_args)

class AlbumCreateView(AlbumMixin,CreateView):
    template_name = "create.html"   
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.get_form_class()
        return context
     
    
    def post(self,request,*args,**kwargs):
        form = self.get_form_class(data=request.POST)
        if form.is_valid():
            if self.request.user.user_type == "artist":
                form.cleaned_data["artist_id"] = self.request.user.artist_profile.id
            self.model.create(**form.cleaned_data)
            messages.success(request,"Album Created.")
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
        
class AlbumUpdateView(AlbumMixin,BaseUpdateView):
    template_name = "update.html"
    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        self.instance = self.get_object()
        if self.request.user.user_type == "artist":
            context["form"] = self.artist_form_class(initial=self.instance.__dict__)
        else:
            context["form"] = self.form_class(initial=self.instance.__dict__,choices=self.get_choices()) 
        return context


    def post(self,request,*args,**kwargs):
        instance = self.get_object()
        if self.request.user.user_type == "artist" :
            form = self.artist_form_class(data=request.POST)
        else:
            form = self.form_class(data=request.POST,choices=self.get_choices())
        if form.is_valid():      
            instance.update(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
class AlbumDeleteView(AlbumMixin,DeleteMixin,View):
     def get(self, request):
        status = self.remove_from_DB(request)
        return JsonResponse({"deleted": status})




class MusicMixin(HasPermissionMixin,PartialTemplateMixin):
    form_class = MusicCreateForm
    model = Music
    success_url = reverse_lazy("music_list")
    template_dir="music/"
    authorized_groups = ["admin","artist"]


    
    def get_choices(self):
        if self.request.user.user_type == "artist":
            albums = Album.filter_from_db(artist_id=self.request.user.artist_profile.id)
        else:
            albums = Album.filter_from_db()
        choices = [(None,"Select Album")]
        for album in albums:
            choices.append((album.id,album.title))
        return choices

class MusicListView(MusicMixin,ListView):
    template_name = "music/music_list.html"
    paginate_by = 10
    authorized_groups = ["admin","artist","artist_manager"]


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["authorized_groups"] = ["admin","artist"]
        return context

    def get_queryset(self):
        search = self.request.GET.get("q")
        album_id = self.request.GET.get("album")
        user = self.request.user
        filter_args = {}
        if search:
            filter_args["title__icontains"] = f"%{search}%"
        if album_id:
            filter_args["album_id"] = int(album_id)

        if user.user_type == "artist":
            return Music.artist_filter(user_id=user.id,**filter_args)
        elif user.user_type == "artist_manager":
            return Music.manager_filter(manager_user_id=user.id,**filter_args)


        

        return Music.filter_from_db(**filter_args)

class MusicCreateView(MusicMixin,CreateView):
    template_name = "create.html"   
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["form"] = self.get_form_class()
        return context
    
    def get_form_class(self,**kwargs):
        return self.form_class(choices=self.get_choices(),**kwargs)
    
    
    def post(self,request,*args,**kwargs):
        form = self.get_form_class(data=request.POST)
        if form.is_valid():
            self.model.create(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
        
class MusicUpdateView(MusicMixin,BaseUpdateView):
    template_name = "update.html"
 
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        self.instance = self.model.get_from_db(id=kwargs.get("pk"))
        context["form"] = self.form_class(initial=self.instance.__dict__,choices=self.get_choices()) 
        return context


    def post(self,request,*args,**kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST,choices=self.get_choices())
        if form.is_valid():      
            instance.update(**form.cleaned_data)
            return redirect(self.success_url)
        return render(request,self.get_template_names(),context={"form":form})
    
class MusicDeleteView(MusicMixin,DeleteMixin,View):
    ...