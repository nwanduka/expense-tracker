from fastapi import FastAPI, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import datetime
import time
from database import SessionLocal, engine, Base, Transaction
from metrics import (
    http_requests_total,
    http_request_duration_seconds,
    transactions_created_total,
    transactions_retrieved_total,
    get_metrics
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware to track all requests
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    
    # Record metrics
    http_requests_total.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()
    
    http_request_duration_seconds.labels(
        method=request.method,
        endpoint=request.url.path
    ).observe(duration)
    
    return response

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

@app.get("/metrics")
def metrics():
    """Prometheus metrics endpoint"""
    return get_metrics()

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
    
    # Track metric
    transactions_created_total.inc()
    
    return {
        "id": db_transaction.id,
        "amount": db_transaction.amount,
        "description": db_transaction.description,
        "date": db_transaction.date.isoformat()
    }

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    
    # Track metric
    transactions_retrieved_total.inc()
    
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