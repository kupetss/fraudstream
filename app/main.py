import json
from fastapi import FastAPI, HTTPException
from producer.producer import send_transaction
from app.schemas.transaction import Transaction

app = FastAPI()

@app.post("/transactions")
def create_transaction(transaction: Transaction):
    data = transaction.model_dump(mode="json")

    try:
        send_transaction(data)
    except Exception as e:
        raise HTTPException(status_code=503, detail="Kafka is unavailable") from e
    
    return{
        "message" : "transaction polychena",
        "transaction" : transaction
    }


@app.get("/")
def home():
    return {"message": "API is running"}

