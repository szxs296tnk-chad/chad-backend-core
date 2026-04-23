from fastapi import FastAPI
from api.routes import router
from infra.middleware import setup_middlewares

app = FastAPI(title="CHAD Final Backend")

setup_middlewares(app)
app.include_router(router)

@app.get("/")
def root():
    return {"status": "running"}
