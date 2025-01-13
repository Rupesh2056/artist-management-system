from django.db import models
import datetime
from enum import Enum
# Create your models here.
from pydantic import BaseModel
from base.exceptions import InvalidAttributeError
from database.operations import execute_select_first_query, execute_select_query

class CustomBaseModel(BaseModel):

    @classmethod
    def get_table_name(cls) -> str:
        '''
        Returns the standard TableName that will be created/ has been created on Database for this model.
        '''
        return cls.__module__.split(".")[0] + "_" + cls.__name__.lower()
    
    @classmethod
    def get_fields(cls) -> list[str]:
        '''
        Returns a list of fields of the Model.
        '''
        return list(cls.model_fields.keys())
    
    def get_values(self):
        values = [self.__getattribute__(field) for field in self.get_fields()]
        return tuple(values)
    
    def get_insert_query(self) -> str:
        '''
        Prepares and Returns a psycopg2 query to insert record into a table.
        Eg: "Insert INTO user_user (full_name,email,...) VALUES (%s,%s,...)"
        '''
        fields = self.get_fields()
        values = ("%s,"*len(fields))[:-1]
        return f'INSERT INTO {self.get_table_name()} ({",".join(fields)}) VALUES ({values})'
    
    @classmethod
    def initialize(cls,data) -> object:
        '''
        Takes in a tuple and returns model Object.
        '''
        object_tuple = data[1:]
        fields = cls.get_fields()
        data = {field:object_tuple[index] for index,field in enumerate(fields) if  object_tuple[index]}

        # data = {}
        # for index,field in enumerate(fields):
        #         if object_tuple[index]:
        #                 data[field] = object_tuple[index] 

        print(data)
        obj = cls(**data)
        return obj

    @classmethod
    def filter_from_db(cls,**kwargs) -> list:
        '''
        Returns list of Model objects after filtering through the database.
        '''
        fields = cls.get_fields()
        queries = []
        values = []
        for key,val in kwargs.items():
            if key in fields:
                queries.append(f"{key} = %s ")
                values.append(val)
            else:
                raise InvalidAttributeError(key,cls)
        sql_query = f'SELECT * FROM {cls.get_table_name()} '        
        if queries:
            sql_query += "WHERE " + "AND".join(queries)
            rows = execute_select_query(sql_query,tuple(values))
        else:
            rows = execute_select_query(sql_query)
        if rows:
            qs = []
            for row in rows:
                model = cls.initialize(row)
                qs.append(model)
            return qs
        
    


    
    @classmethod
    def get_from_db(cls,**kwargs) -> object:
        '''
        Returns a Model Object from Database.
        '''
        fields = cls.get_fields()
        queries = []
        values = []
        for key,val in kwargs.items():
            if key in fields:
                queries.append(f"{key} = %s ")
                values.append(val)
        sql_query = f'SELECT * FROM {cls.get_table_name()} '        
        if queries:
            sql_query += "WHERE " + "AND".join(queries)
            object_tuple = execute_select_first_query(sql_query,tuple(values))
        else:
            object_tuple = execute_select_first_query(sql_query)

        if object_tuple:
            return cls.initialize(object_tuple)
        else:
            return None
        
    def __str__(self):
        return f"<{self.__class__.__name__}>"

        


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

    def __str__(self):
        return f"<{self.__class__.__name__}:{self.email}>"
    
    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.email}>"
        
    






        



