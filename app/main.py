from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

# Connect to Redis
redis_port = os.getenv("REDIS_PORT")
redis_host = os.getenv("REDIS_HOST")
redis_db = os.getenv("REDIS_DB")
r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

# Test Redis connection
try:
    r.ping()
    print("Redis connected.")
except redis.ConnectionError:
    raise Exception("Redis connection failed.")


@app.get("/")
def root():
    r.set("foo", "bar")
    return {"message": "Hello World", "redis_value": r.get('foo')}
