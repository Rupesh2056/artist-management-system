from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password,check_password
from base.mixins import LoginRequiredMixin
from database.operations import execute_insert_query
from user.models import User

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
        return render(request,"music/index.html")
    

# class CustomLoginView
