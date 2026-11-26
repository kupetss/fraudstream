import json
import logging
from kafka import KafkaConsumer
from database.repository import save_transaction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    group_id="fraud-detection",
    auto_offset_reset="earliest"
)

def analyze_transaction(data:dict):
    is_fraud = data["amount"] >= 10000

    if is_fraud:
        logging.warning(f"Fraud alert! {data}")
    else:
        logging.info("Transaction is safe: {data}")

    save_transaction(data, is_fraud)
    logging.info("Transaction saved to PostgreSQL")

for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    analyze_transaction(data)