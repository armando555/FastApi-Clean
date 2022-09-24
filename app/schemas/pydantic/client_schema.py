from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Client

ClientSchema = pydantic_model_creator(Client)
ClientSchemaCreate = pydantic_model_creator(Client, name=f'{Client.__name__}SchemaCreate', exclude_readonly=True)