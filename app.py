from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes import orders, metrics
from database import init_db


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Order Processing API",
        version="1.0.0",
        description="API for managing and processing e-commerce orders",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()
app.openapi = custom_openapi


@app.on_event("startup")
async def startup_event():
    init_db()
    # asyncio.create_task(process_orders())

app.include_router(orders.order_router)
app.include_router(metrics.metric_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=3000,
        reload=True,
    )