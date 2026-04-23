from fastapi import FastAPI, Request
import time

def setup_middlewares(app: FastAPI):
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start
        print(f"{request.method} {request.url} - {duration:.3f}s")
        return response
