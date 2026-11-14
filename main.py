from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(title="MotorGuard Backend")

class TelemetryData(BaseModel):
    device_id: str
    rpm: float
    current: float
    voltage: float
    power: float
    vibration: float
    acoustic: Optional[float] = None
    temperature: Optional[float] = None
    motor_status: str = "RUNNING"
    protection_state: str = "NORMAL"


latest_data = {}


@app.get("/")
def home():
    return {
        "message": "MotorGuard Backend is Running!",
        "status": "online"
    }


@app.post("/telemetry")
def receive_telemetry(data: TelemetryData):
    global latest_data

    latest_data = {
        "device_id": data.device_id,
        "rpm": data.rpm,
        "current": data.current,
        "voltage": data.voltage,
        "power": data.power,
        "vibration": data.vibration,
        "acoustic": data.acoustic,
        "temperature": data.temperature,
        "motor_status": data.motor_status,
        "protection_state": data.protection_state,
        "timestamp": datetime.now().isoformat()
    }

    print("Received telemetry:", latest_data)

    return {
        "status": "success",
        "message": "Telemetry received successfully"
    }


@app.get("/latest")
def get_latest():
    return latest_data