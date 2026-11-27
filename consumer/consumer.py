import json
import logging
from kafka import KafkaConsumer
from database.repository import save_transaction
from kafka import TopicPartition
from kafka.structs import OffsetAndMetadata

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    group_id="fraud-detection",
    auto_offset_reset="earliest",
    enable_auto_commit=False,
    value_deserializer=lambda x:json.loads(x.decode("utf-8"))
)

def analyze_transaction(data: dict):
    is_fraud = data["amount"] >= 10000

    saved = save_transaction(data, is_fraud)

    if not saved:
        return

    if is_fraud:
        logging.warning(f"Fraud alert! {data}")
    else:
        logging.info(f"Transaction is safe: {data}")

    logging.info("Transaction saved to PostgreSQL")
    
for message in consumer:
    try:
        analyze_transaction(message.value)
        partition = TopicPartition(message.topic, message.partition)
        offset = OffsetAndMetadata(message.offset + 1, "", -1)
        consumer.commit({partition:offset})
        logging.info(f"Offset committed: {message.offset + 1}")

    except Exception:
        logging.exception("Transaction processing failed")
        raise