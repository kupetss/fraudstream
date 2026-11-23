import json
import time
import logging
from kafka import KafkaProducer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092"
)

def send_transaction(data: dict):
    message = json.dumps(data).encode("utf-8")
    for temp in range(5):
        try:
            producer.send("transactions", message).get(timeout=10)
            logging.info("Transaction is over")
            return
        except Exception as e:
            if temp == 4:
                logging.exception("Cannot send transaction")
                raise

            logging.warning(f"Try № {temp + 1}. Error sending transaction: {e}")
            time.sleep(2)
