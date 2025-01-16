from django.db import models

from database.base import CustomBaseModel
import datetime
from enum import Enum

from user.models import User
from typing import Optional

# Create your models here.
class GenreEnum(str,Enum):
    RNB = "rnb"
    Classic = "classic"
    Country = "country"
    Rock = "rock"
    Jazz = "jazz"
    Funk = "funk"
    Metal = "metal"

class Artist(CustomBaseModel):
    id : int = None
    user_id : int = None
    first_album_release_year : Optional[int]  = None
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()


    class Meta:
        foreign_keys = {"user_id":User}
        read_only_fields = ["id"]


    

class Album(CustomBaseModel):
    id : int =None
    title : str
    artist_id : int
    release_date : datetime.date = None
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()


    class Meta:
        foreign_keys = {"artist_id":Artist}
        read_only_fields = ["id"]


class Music(CustomBaseModel):
    id : int = None
    album_id : int 
    title : str
    genre : GenreEnum
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()

    class Meta:
        foreign_keys = {"album_id":Album}
        read_only_fields = ["id"]


    
        
