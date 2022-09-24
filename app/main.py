from fastapi import Depends, FastAPI
from app.configs.environment import get_environment_variables
from tortoise import Tortoise
import uvicorn

from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION
)


register_tortoise(
    app,
    db_url="mysql://root:root@localhost:33061/test_bookstore",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
#Init database
Tortoise.init_models(['app.models'], 'models')

from app.routers.v1 import DepartmentRouter,CityRouter,ClientRouter

# Add Routers
app.include_router(DepartmentRouter)
app.include_router(CityRouter)
app.include_router(ClientRouter)







def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, debug=True)