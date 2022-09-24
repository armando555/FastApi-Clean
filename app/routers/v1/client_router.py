
from fastapi_crudrouter import TortoiseCRUDRouter
from app.models import Client
from app.schemas.pydantic import ClientSchema, ClientSchemaCreate


ClientRouter = TortoiseCRUDRouter(
    schema=ClientSchema,
    create_schema=ClientSchemaCreate,
    db_model=Client,
    prefix=Client.__name__
)
