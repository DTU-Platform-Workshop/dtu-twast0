import signal
import sys
import os

from fastapi import Body, FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Hello at {os.getenv('PORT', '4242')}", flush=True)
    yield
    print(f"Shutting down!", flush=True)

app = FastAPI(title='app', lifespan=lifespan)

@app.get('/readyz')
@app.get('/livez')
@app.get('/')
def hello():
    return f"Hello World!"

def terminate(signal, frame):
    sys.exit(0)

if __name__ == '__main__':
    import uvicorn

    signal.signal(signal.SIGTERM, terminate)
    port = int(os.getenv("PORT", "4242"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")