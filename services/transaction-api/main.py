from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from database import SessionLocal, engine, Base, Transaction

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello from your expense tracker!"}

@app.post("/transactions")
def create_transaction(amount: float, description: str, db: Session = Depends(get_db)):
    # Create new transaction
    db_transaction = Transaction(
        amount=amount,
        description=description,
        date=datetime.now()
    )
    
    # Add to database
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return {
        "id": db_transaction.id,
        "amount": db_transaction.amount,
        "description": db_transaction.description,
        "date": db_transaction.date.isoformat()
    }

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    
    return {
        "transactions": [
            {
                "id": t.id,
                "amount": t.amount,
                "description": t.description,
                "date": t.date.isoformat()
            }
            for t in transactions
        ],
        "total": len(transactions)
    }