from pydantic import BaseModel
from base.exceptions import InvalidAttributeError
from database.operations import execute_db_query, execute_insert_query, execute_select_first_query, execute_select_query
import datetime
from pydantic._internal._model_construction import ModelMetaclass
import importlib

class CRUDMixin:
    @classmethod
    def create(cls,**kwargs):
        obj = cls(**kwargs)
        query  = cls.get_insert_query()
        values = obj.get_values(exclude=["id"])
        print(query)
        print(values)
        execute_insert_query(query,values)
        return obj
    
    @classmethod
    def delete(cls,**kwargs):
        fields = cls.get_fields()
        queries = []
        values = []
        for key,val in kwargs.items():
            if key in fields:
                queries.append(f"{key} = %s ")
                values.append(val)
            else:
                raise InvalidAttributeError(key,cls)
        sql_query = f'DELETE FROM {cls.get_table_name()} '        
        if queries:
            sql_query += "WHERE " + "AND".join(queries)
            execute_db_query(sql_query,tuple(values))
        else:
            execute_db_query(sql_query)

    def update(self,**kwargs):
        update_fields = []
        update_values = []
        update_fields_query = ""

        for field,value in kwargs.items():
            if field in self.get_fields():
                update_fields.append(f"{field}=%s ")
                update_values.append(value)
            else:
                raise InvalidAttributeError(field,self.__class__.__name__)
        if update_fields:
            update_fields_query += ",".join(update_fields) + f", updated_at=%s "
        
            update_values.append(datetime.datetime.now())
            update_values.append(self.id) # append the id for where clause
            sql_query = f'UPDATE {self.get_table_name()} SET {update_fields_query} WHERE id=%s'
            execute_db_query(sql_query,tuple(update_values))

    def save(self):
        update_fields = []
        update_values = []
        for field in self.get_insert_fields():
            if field in self.get_fields():
                update_fields.append(f"{field}=%s ")
                update_values.append(self.__getattribute__(field) if field !="updated_at" else datetime.datetime.now() )
            else:
                raise InvalidAttributeError(field,self.__class__.__name__)
        if update_fields:
            update_fields_query = ",".join(update_fields)
        
            update_values.append(self.id) # append the id for where clause
            sql_query = f'UPDATE {self.get_table_name()} SET {update_fields_query} WHERE id=%s'
            execute_db_query(sql_query,tuple(update_values))

def import_class(full_class_name: str):
    """
    Dynamically import a class from a fully qualified name.
    """
    module_name, class_name = full_class_name.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

class ForeignKeyMeta(ModelMetaclass,type):
    def __new__(cls, name, bases, dct):
        # Create the new class
        new_cls = super().__new__(cls, name, bases, dct)

        foreign_keys = getattr(new_cls.Meta, "foreign_keys", {})
        for foreign_key_field,related_name in foreign_keys.items():
            # Define a dynamic property for each foreign key
            def foreign_key_property(self, related_name=related_name, foreign_key_field=foreign_key_field):
                foreign_key_value = getattr(self, foreign_key_field, None)
                if foreign_key_value is not None:
                    related_class = related_name
                    if related_class and hasattr(related_class, "get_from_db"):
                        return related_class.get_from_db(id=foreign_key_value)
                return None
            # Add the property to the class
            setattr(new_cls, related_name.__name__.lower(), property(foreign_key_property))

        return new_cls


class CustomBaseModel(CRUDMixin,BaseModel,metaclass=ForeignKeyMeta):

    class Config:  
        use_enum_values = True

    def __str__(self):
        return f"<{self.__class__.__name__}>"
    
    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    
    class Meta:
        read_only_fields = ["id"]
    
    def get_values(self,exclude=None):
        if exclude:
            values = [self.__getattribute__(field) for field in self.get_fields() if field not in exclude]
        else:
            values = [self.__getattribute__(field) for field in self.get_fields()]
        return tuple(values)
    

    
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
    
    @classmethod
    def get_insert_fields(cls) -> list[str]:
        '''
        Returns a list of fields of the Model.
        '''
        return list(field for field in cls.model_fields.keys() if field not in cls.Meta.read_only_fields)
    
    @classmethod
    def get_insert_query(self) -> str:
        '''
        Prepares and Returns a psycopg2 query to insert record into a table.
        Eg: "Insert INTO user_user (full_name,email,...) VALUES (%s,%s,...)"
        '''
        fields = self.get_insert_fields()
        values = ("%s,"*len(fields))[:-1]
        return f'INSERT INTO {self.get_table_name()} ({",".join(fields)}) VALUES ({values})'
    
    @classmethod
    def initialize(cls,data) -> object:
        '''
        Takes in a tuple and returns model Object.
        '''
        object_tuple = data
        fields = cls.get_fields()
        data = {field:object_tuple[index] for index,field in enumerate(fields) if  object_tuple[index]}

        # data = {}
        # for index,field in enumerate(fields):
        #         if object_tuple[index]:
        #                 data[field] = object_tuple[index] 

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