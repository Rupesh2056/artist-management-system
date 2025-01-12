from django.db import models
import datetime
from enum import Enum
# Create your models here.
from pydantic import BaseModel


class GenderEnum(str,Enum):
    Male = "m"
    Female = "f"
    Other = "o"

class UserTypeEnum(str,Enum):
    Admin = "admin"
    ArtistManager = "artist_manager"
    Artist = "artist"

    def __repr__(self) -> str:
        return str.__repr__(self.value)



class User(BaseModel):
    full_name : str
    email : str
    address : str = None
    phone : str = None
    dob : datetime.date = None  
    gender : GenderEnum = None
    user_type : UserTypeEnum = UserTypeEnum.Artist
    password : str
    created_at : datetime.datetime = None
    updated_at : datetime.datetime = datetime.datetime.now()

    class Config:  
        use_enum_values = True
        
    @classmethod
    def get_fields(cls):
        return list(cls.model_fields.keys())
    
    def get_values(self):
        values = [self.__getattribute__(field) for field in self.get_fields()]
        return tuple(values)
    
    def get_insert_query(self):
        fields = self.get_fields()
        values = ("%s,"*len(fields))[:-1]
        return f'INSERT INTO "{self.__class__.__name__}" ({",".join(fields)}) VALUES ({values})'
        # return f'INSERT INTO "{self.__class__.__name__}" ({",".join(self.get_fields())}) VALUES {self.get_values()}'

    # def get_objec





        



