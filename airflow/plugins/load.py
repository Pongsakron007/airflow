import psycopg2
import json

def load(**context):
    file_path = context['ti'].xcom_pull(task_ids='fetch_price')
    
    with open(file_path, "r") as f:
        data = json.load(f)
        price_str = data["price"]

    # ✅ แปลง string ที่มี , ให้เป็น float ก่อน
    price_clean = float(price_str.replace(",", ""))

    conn = psycopg2.connect(
        dbname="gold_db", user="airflow", password="airflow", host="postgres"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO gold_price (price, fetched_at) VALUES (%s, now());",
        (price_clean,)
    )
    conn.commit()
    cur.close()
    conn.close()