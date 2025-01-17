from base.utils import ExportMixin
from django.views import View

from music.models import Artist
from user.forms import ArtistBulkUploadForm
from user.models import User
from user.views import ArtistListView
import pandas as pd
from pydantic import ValidationError

class ArtistExportView(ExportMixin, View):
    fields = [
        "SN",
        "email",
        "full_name",
        "Address",
        "Phone",
        "DOB",
        "Gender",
        "First Album Release Year",
        "Created at",
        "Updated at",
    ]

    def get_queryset(self, *args, **kwargs):
        return ArtistListView.get_artist_list_queryset(self.request)
    
    name = "Artists"

    def write_rows(self, writer, queryset):
        for index,object in enumerate(queryset):
            
      
            
            writer.writerow(
                [
                    index +1,
                    object.email,
                    object.full_name,
                    object.address,
                    object.phone,
                    object.dob,
                    object.gender,
                    object.artist_profile.first_album_release_year,
                    object.created_at.strftime("%d %b %Y, %I:%M %p"),
                    object.updated_at.strftime("%d %b %Y, %I:%M %p"),
                ]
            )

import os
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password
class BulkUploadView(View):
    template_name = "upload.html"
    def get(self,request,*args,**kwargs):
        context = {}
        context["form"] = ArtistBulkUploadForm
        return render(request,"upload.html",context)

    def post(self, request,*args,**kwargs):
        print("posttttt9")
        errors = []
        context = {}
        user = request.user
        if user.user_type == "artist_manager":
            artist_manager_id = user.id
        else:
            artist_manager_id = None

        failure_count = 0
        upload_count = 0
        try:
            form = ArtistBulkUploadForm(request.POST,files=request.FILES)
            if form.is_valid():
                context["form"] = form
                file = form.cleaned_data.get("csv_file")

                file_name = file.name
                split_tup = os.path.splitext(file_name)
                file_extension = split_tup[1]
                if not file_extension == ".csv":       
                    context["message"] = "Please provide .csv file"
                    messages.error(request,"Please provide .csv file.")
                    return render(request,self.template_name,context)
    
                code_header = 'Code'
                full_name_header = 'Full Name'
                email_header = 'Email'
                address_header = 'Address'
                phone_header = "Phone"
                dob_header = "DOB"
                gender_header = "Gender"
                first_album_header = "First Album Release Year"
                password_header = "Password"

                headers_list = [code_header,full_name_header,email_header,address_header,phone_header,
                            dob_header,gender_header,first_album_header,password_header,
                            ]
                
                df = pd.read_csv(file).fillna('')
                
                check =  all(item in df.columns for item in headers_list)
                if not check:
                    headers_list_string = ""
                    for x in headers_list:
                        if x not in df.columns:
                            headers_list_string = headers_list_string + x + ","
          
                    context["message"] = "Check if File has proper column names ." + headers_list_string
                    return render(request,self.template_name,context)
                for row in range(0, len(df)):
                    try:
                        code = df[code_header][row]
                        full_name = df[full_name_header][row]
                        email = df[email_header][row]
                        address = df[address_header][row]           
                        phone = df[phone_header][row]           
                        dob = df[dob_header][row]           
                        gender = df[gender_header][row]    
                        first_album =   df[first_album_header][row]      
                        password =   df[password_header][row]  
                        
                        if not all([code,full_name,email,password]):
                            context["message"] = "Check if File has proper values" 
                            return render(request,self.template_name,context)
                        dob = dob.replace("/","-") if dob else None
                        phone = str(phone) if phone else None
                        first_album = int(first_album) if first_album else None
                        first_album = int(first_album) if first_album else None
                        try:
                            user = User.create(full_name=full_name,
                                        email = email,
                                        address = address,
                                        phone = phone,
                                        dob = dob,
                                        gender = gender,
                                        password = make_password(password) 
                                        )
                            Artist.create(user_id=user.id,first_album_release_year=first_album,
                                          artist_manager_id=artist_manager_id)
                            upload_count += 1

                        except ValidationError as e:
                            error_message = "; ".join([f"{err['loc'][0]}: {err['msg']}" for err in e.errors()])
                            print(error_message)
                            errors.append({f'code':code , 'error':error_message})
                            failure_count += 1

        
                    except Exception as e:
                        failure_count += 1
                        messages.error(request,f"{code} : {str(e)}")
                        errors.append({f'code':code , 'error':str(e)})


            context["upload_count"] = upload_count
            context["failure_count"] = failure_count
            context["errors"] = errors
            return render(request,self.template_name,context)

        except Exception as e:
            context["message"] = "Data Upload Failed"
            context["error"] = str(e)
            messages.error(request,f"Upload Failed. {str(e)}")
            return render(request,self.template_name,context)

