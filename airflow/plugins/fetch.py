import os
import json
import requests
from datetime import datetime

def fetch():
    response = requests.get("https://api.chnwt.dev/thai-gold-api/latest")
    data = response.json()
    price = data["response"]["price"]["gold"]["buy"]

    # บันทึกลงไฟล์
    dir_path = "/opt/airflow/shared"  # shared volume ที่ Airflow เห็น
    os.makedirs(dir_path, exist_ok=True)
    filename = f"gold_price_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    full_path = os.path.join(dir_path, filename)

    with open(full_path, "w") as f:
        json.dump({"price": price}, f)

    return full_path  # ✅ ส่ง path แทนข้อมูล


response = requests.get("https://api.chnwt.dev/thai-gold-api/latest")
print(response)