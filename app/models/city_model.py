from tortoise.models import Model
from tortoise import fields

class City(Model):
    id = fields.IntField(pk=True)
    code_city = fields.CharField(max_length=3)
    city_name = fields.CharField(max_length=150)
    code_dane = fields.CharField(max_length=10)
    
    department = fields.ForeignKeyField(
        model_name='models.Department',
        related_name='cities'
    )

    def __repr__(self):
        return f'{self.id} | {self.code_city} | {self.city_name}'