# Transaction API

A FastAPI-based service for managing financial transactions.

## Running Locally
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000/docs for interactive API documentation.

## Running with Docker
```bash
# Build the image
docker build -t expense-tracker-api .

# Run the container
docker run -p 8000:8000 expense-tracker-api
```

## API Endpoints

- `GET /` - Welcome message
- `POST /transactions` - Create a new transaction
- `GET /transactions` - Retrieve all transactions

## Current Limitations

- Data is stored in memory and lost on restart
- No database persistence yet
- No authentication