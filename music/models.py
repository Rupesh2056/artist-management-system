from django.db import models

from base.exceptions import InvalidAttributeError
from database.base import CustomBaseModel
import datetime
from enum import Enum

from database.operations import execute_select_query
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
    artist_manager_id : Optional[int] = None
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
                    SELECT * FROM {cls.get_table_name()} album JOIN {Artist.get_table_name()} artist ON
                    album.artist_id=artist.id  WHERE artist.artist_manager_id=%s """      
        if queries:  
            sql_query +=  " AND "  + "AND".join(queries)
        rows = execute_select_query(sql_query,tuple(values))
        if rows:
            qs = []
            for row in rows:
                model = cls.initialize(row)
                qs.append(model)
            return qs
        return []
    

    





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



    @classmethod
    def manager_filter(cls,manager_user_id,**kwargs):
        fields = cls.get_fields()
        queries = []
        values = [manager_user_id]
        for key,val in kwargs.items():
            actual_field_name = key.split('__')[0]
            if  actual_field_name in fields:
                if "__" in key:
                    queries.append(f" Lower(music.{actual_field_name}) LIKE %s ")
                    values.append(f"%{val}%")
                else:
                    queries.append(f"{key} = %s ")
                    values.append(val)
            else:
                raise InvalidAttributeError(key,cls)
        sql_query = f"""
                    SELECT * FROM {cls.get_table_name()} music JOIN {Album.get_table_name()} album on music.album_id=album.id
                    JOIN {Artist.get_table_name()} artist ON
                    album.artist_id = artist.id where artist.artist_manager_id=%s """       

        if queries:
            sql_query +=" AND " + "AND".join(queries)
        rows = execute_select_query(sql_query,tuple(values))
        if rows:
            qs = []
            for row in rows:
                model = cls.initialize(row)
                qs.append(model)
            return qs
        return []
    

    @classmethod
    def artist_filter(cls,user_id,**kwargs):
        fields = cls.get_fields()
        queries = []
        values = [user_id]
        for key,val in kwargs.items():
            actual_field_name = key.split('__')[0]
            if  actual_field_name in fields:
                if "__" in key:
                    queries.append(f" Lower(music.{actual_field_name}) LIKE %s ")
                    values.append(f"%{val}%")
                else:
                    queries.append(f"{key} = %s ")
                    values.append(val)
            else:
                raise InvalidAttributeError(key,cls)
        sql_query = f"""
                    SELECT * FROM {cls.get_table_name()} music JOIN {Album.get_table_name()} album ON
                    album.id=music.album_id JOIN {Artist.get_table_name()} artist on album.artist_id=artist.id JOIN
                    user_user u on u.id=artist.user_id where u.id=%s """    
        if queries:    
            sql_query += " AND " + " AND ".join(queries)
        rows = execute_select_query(sql_query,tuple(values))
        if rows:
            qs = []
            for row in rows:
                model = cls.initialize(row)
                qs.append(model)
            return qs
        return []
    



    
        
