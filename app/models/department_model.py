from typing import TYPE_CHECKING
from tortoise.models import Model
from tortoise import fields

if TYPE_CHECKING:
    from .city_model import City
    

class Department(Model):
    __tablename__ = "departments"
    id = fields.IntField(pk=True)

    code_department = fields.CharField(max_length=3)
    department_name = fields.CharField(max_length=150)
    small_name = fields.CharField(max_length=150)
    code_dane = fields.CharField(max_length=10)
    
    cities = fields.ReverseRelation['City']
    
    def __repr__(self):
        return f'{self.id} | {self.code_department} | {self.department_name}'