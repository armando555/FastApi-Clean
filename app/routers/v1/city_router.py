
from fastapi_crudrouter import TortoiseCRUDRouter
from app.models import City
from app.schemas.pydantic import CitySchema, CitySchemaCreate


CityRouter = TortoiseCRUDRouter(
    schema=CitySchema,
    create_schema=CitySchemaCreate,
    db_model=City,
    prefix=City.__name__
)
@CityRouter.get("/test")
def test():
    return "Hola"