from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Department

DepartmentSchema = pydantic_model_creator(Department)
DepartmentSchemaCreate = pydantic_model_creator(Department, name=f'{Department.__name__}SchemaCreate', exclude_readonly=True)