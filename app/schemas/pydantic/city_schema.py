from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import City

CitySchema = pydantic_model_creator(City)
CitySchemaCreate = pydantic_model_creator(City, name=f'{City.__name__}SchemaCreate', exclude_readonly=True)