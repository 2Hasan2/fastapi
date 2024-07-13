from fastapi import FastAPI
from .database import create_db, SessionLocal
from .routes.auth import router as auth_router
from .routes.categories import router as categories_router
from .routes.products import router as products_router
from .middlewares import CustomMiddleware
from .config import DATABASE_URL
from databases import Database

# Initialize database connection
database = Database(DATABASE_URL)

def create_app() -> FastAPI:
    app = FastAPI()

    # /auth/* routes
    app.include_router(auth_router, prefix="/auth", tags=["users"])

    # /categories/* routes
    app.include_router(categories_router, prefix="/categories", tags=["categories"])

    # /products/* routes
    app.include_router(products_router, prefix="/products", tags=["products"])

    # Add custom middleware
    app.add_middleware(CustomMiddleware)

    @app.on_event("startup")
    async def startup():
        await database.connect()
        create_db()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app

app = create_app()
