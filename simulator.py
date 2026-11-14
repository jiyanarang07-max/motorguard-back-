import requests
import random
import time

URL = "http://127.0.0.1:8000/telemetry"

while True:
    rpm = round(random.uniform(1500, 1580), 2)
    current = round(random.uniform(0.9, 1.2), 2)
    voltage = round(random.uniform(11.8, 12.3), 2)
    power = round(voltage * current, 2)
    vibration = round(random.uniform(0.20, 0.35), 3)
    acoustic = round(random.uniform(0.15, 0.30), 3)
    temperature = round(random.uniform(30, 40), 2)

    telemetry = {
        "device_id": "MotorGuard-01",
        "rpm": rpm,
        "current": current,
        "voltage": voltage,
        "power": power,
        "vibration": vibration,
        "acoustic": acoustic,
        "temperature": temperature,
        "motor_status": "RUNNING",
        "protection_state": "NORMAL"
    }

    try:
        response = requests.post(URL, json=telemetry)
        print("Sent:", telemetry)
        print("Server response:", response.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(2)