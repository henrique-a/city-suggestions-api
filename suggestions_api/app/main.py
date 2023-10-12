import time
import uvicorn
from fastapi import FastAPI
from routers import router
from config import HOST, PORT, UVICORN_WORKERS_COUNT, ENVIRONMENT
from db.client import es
from db.index import cities_index, index_settings, cities_mapping, index_city_data


app = FastAPI(title="City suggestion API")


@app.on_event("startup")
async def startup() -> None:
    time.sleep(30)  # Wait elasticsearch start
    if not es.indices.exists(index=cities_index):
        es.indices.create(index=cities_index, body={"settings": index_settings, "mappings": cities_mapping})
        index_city_data()


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        workers=UVICORN_WORKERS_COUNT,
        reload=ENVIRONMENT == "local",
        reload_dirs=["./"] if ENVIRONMENT == "local" else [],
    )
