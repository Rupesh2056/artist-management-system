import datetime
from enum import Enum
from database.base import CustomBaseModel, import_class
from typing import Optional

# Create your models here.
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


class User(CustomBaseModel):
    id : int = None
    full_name : str
    email : str
    address : str = None
    phone : str = None
    dob : Optional[datetime.date] = None 
    gender : GenderEnum = None
    user_type : UserTypeEnum = UserTypeEnum.Artist
    password : str
    created_at : datetime.datetime = datetime.datetime.now()
    updated_at : datetime.datetime = datetime.datetime.now()

    class Config:  
        use_enum_values = True
    
    class Meta:
        read_only_fields = ["id"]

    
    @property
    def artist_profile(self):
        if self.user_type == "artist":
            return import_class("music.models.Artist").get_from_db(user_id=self.id)
   

    def __str__(self):
        return f"<{self.__class__.__name__}:{self.email}>"
    
    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.email}>"
        
    






        



