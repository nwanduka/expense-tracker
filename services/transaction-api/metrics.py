from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response
import time

# Define metrics
http_requests_total = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

transactions_created_total = Counter(
    'transactions_created_total',
    'Total transactions created'
)

transactions_retrieved_total = Counter(
    'transactions_retrieved_total', 
    'Total times transactions were retrieved'
)

def get_metrics():
    """Endpoint to expose metrics for Prometheus"""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)