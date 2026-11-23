import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from producer import send_transaction

app = FastAPI()

class Transaction(BaseModel):
    user_id: int = Field(gt=0)
    amount: float = Field(gt=0)
    currency: str = Field(min_length=3, max_length=3)


@app.post("/transactions")
def create_transaction(transaction: Transaction):
    data = transaction.model_dump()

    try:
        send_transaction(data)
    except Exception as e:
        raise HTTPException(status_code=503, detail="Kafka is unavaible") from e
    
    return{
        "message" : "transaction polychena",
        "transaction" : transaction
    }


@app.get("/")
def home():
    return {"mwssage": "API is running"}

