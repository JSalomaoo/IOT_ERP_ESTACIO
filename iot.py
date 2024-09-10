import requests
import json
from datetime import datetime, time
import random

url = 'http://localhost:5000/data'

while True:
    data = {
        'sensor_id': 'sensor_01',
        'timestamp': datetime.utcnow().isoformat(),
        'value': random.uniform(20.0, 30.0)
    }
    response = requests.post(url, json=data)
    print(response.json())
    time.sleep(10)  # Enviar dados a cada 10 segundos
