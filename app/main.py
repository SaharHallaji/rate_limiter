from fastapi import FastAPI
import redis
import os

app = FastAPI()

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)


@app.get("/")
async def read_root():
    await r.set('foo', 'bar')
    return {"message": "Hello World", "redis_value": r.get('foo')}
