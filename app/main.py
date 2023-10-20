from fastapi import FastAPI
import uvicorn

from api.routers import hello_world, links
from init_table import init_table



app = FastAPI()
app.include_router(hello_world.router)
app.include_router(links.router)
init_table()
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
