import datetime
from enum import Enum
from base.exceptions import InvalidAttributeError
from database.base import CustomBaseModel, import_class
from typing import Optional

from database.operations import execute_select_query

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
    address : Optional[str] = None
    phone : Optional[str] = None
    dob : Optional[datetime.date] = None 
    gender : Optional[GenderEnum] = None
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
    
    
    @classmethod
    def manager_filter(cls,manager_user_id,**kwargs):
        fields = cls.get_fields()
        queries = []
        values = [manager_user_id]
        for key,val in kwargs.items():
            actual_field_name = key.split('__')[0]
            if  actual_field_name in fields:
                if "__" in key:
                    queries.append(f" Lower({actual_field_name}) LIKE %s ")
                    values.append(f"%{val}%")
                else:
                    queries.append(f"{key} = %s ")
                    values.append(val)
            else:
                raise InvalidAttributeError(key,cls)
        sql_query = f"""
                    SELECT * FROM {cls.get_table_name()} u  JOIN music_artist artist ON
                    artist.user_id=u.id WHERE artist.artist_manager_id=%s """ 

        if queries:    
            # pass   
            sql_query += " AND "  + "AND".join(queries)

        print(sql_query , tuple(values))

        
        rows = execute_select_query(sql_query,tuple(values,))
        if rows:
            qs = []
            for row in rows:
                model = cls.initialize(row)
                qs.append(model)
            return qs
        return []
        
    






        



