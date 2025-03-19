from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

from .sensor import SensorData

app = FastAPI()
sensor = SensorData()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Sensor Dashboard API"}

@app.get("/current")
async def get_current_reading():
    """Get the current sensor reading."""
    return sensor.generate_reading()

@app.get("/stream")
async def stream_data():
    """Stream sensor data using Server-Sent Events."""
    async def event_generator():
        while True:
            data = sensor.generate_reading()
            yield {
                "event": "sensor_update",
                "data": json.dumps(data)
            }
            await asyncio.sleep(2)  # Update every 2 seconds
    
    return EventSourceResponse(event_generator())