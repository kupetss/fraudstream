import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    group_id="fraud-detection-test",
    auto_offset_reset="earliest"
)

def analyze_transaction(data:dict):
    if data["amount"] >= 10000:
        logging.warning("Fraud alert!")
    else:
        logging.info("Transaction is safe")

for message in consumer:
    data = json.loads(message.value.decode("utf-8"))
    analyze_transaction(data)