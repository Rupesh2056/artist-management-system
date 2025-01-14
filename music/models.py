from django.db import models

from database.base import CustomBaseModel
import datetime
from enum import Enum

from user.models import User

# Create your models here.
class GenreEnum(str,Enum):
    RNB = "rnb"
    Classic = "classic"
    Country = "country"
    Rock = "rock"
    Jazz = "jazz"
    funk = "Funk"
    metal = "Metal"

class Artist(CustomBaseModel):
    id : int = None
    user_id : int = None
    first_album_release_year : int  = None
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()


    class Meta:
        foreign_keys = {"user":"user_id"}

    def user(self):
        if self.user_id:
            return User.get_from_db(id=self.user_id)
        
    # def __getattribute__(self, name):
    #     if name in self.Meta.foreign_keys:
    #         id = self.__getattribute__(self.Meta.foreign_keys[name])
    #         if id:
    #             return User.get_from_db(id=id)

        # return super().__getattribute__(name)


    

class Album(CustomBaseModel):
    id : int =None
    artist_id : int
    title : str
    release_date : datetime.date = None
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()


class Music(CustomBaseModel):
    id : int = None
    album_id : int 
    title : str
    genre : GenreEnum
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()


    
        
