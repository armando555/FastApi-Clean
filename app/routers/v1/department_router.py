
from fastapi_crudrouter import TortoiseCRUDRouter
from app.models import Department
from app.schemas.pydantic import DepartmentSchema, DepartmentSchemaCreate


DepartmentRouter = TortoiseCRUDRouter(
    schema=DepartmentSchema,
    create_schema=DepartmentSchemaCreate,
    db_model=Department,
    prefix=Department.__name__
)
