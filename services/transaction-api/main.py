from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# This will store our transactions in memory (temporary)
transactions = []

@app.get("/")
def read_root():
    return {"message": "Hello from your expense tracker!"}

@app.post("/transactions")
def create_transaction(amount: float, description: str):
    transaction = {
        "id": len(transactions) + 1,
        "amount": amount,
        "description": description,
        "date": datetime.now().isoformat()
    }
    transactions.append(transaction)
    return transaction

@app.get("/transactions")
def get_transactions():
    return {"transactions": transactions, "total": len(transactions)}