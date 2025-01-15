from django.shortcuts import render
from django.views import View
from base.mixins import LoginRequiredMixin
from music.models import Artist
# Create your views here.

class IndexView(LoginRequiredMixin,View):
    
    def get(self,request,*args,**kwargs):

        # print(request.user.is_authenticated)
        # password = "password"
        # hashed_password = make_password(password)
        # # print(hashed_password)
        # # print(check_password(password,hashed_password))
        # create_user_query = 'INSERT INTO "User" (full_name,email,address,phone) VALUES (%s,%s,%s,%s) '
        # values = ("Rupesh Chaulagain","email","address","phone ")
        # execute_insert_query(create_user_query,values)
        # print("done ")

        # u = User(full_name="Rupesh",email="rupesh@asparksys.com",password="abcd")
        # # print(u)
        # # u.get_fields()
        # print(u.get_insert_query())
        # users = User.filter_from_db(gender="m")
        # print(users)
        # Artist.create(first_album_release_year=2000)
        artist = Artist.get_from_db(id=1)
        # print(artist.user.full_name)
        context = {}

        return render(request,"music/index.html",context)
    






