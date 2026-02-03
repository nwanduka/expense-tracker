import re
import os
import time
from imapclient import IMAPClient
from dotenv import load_dotenv
import requests
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup

# Import parsers
from parsers.sterling_parser import SterlingBankParser

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
IMAP_SERVER = os.getenv('IMAP_SERVER')
API_URL = os.getenv('API_URL', 'http://localhost:8000')

# Initialize parsers
PARSERS = [
    SterlingBankParser(),
    # Add more parsers here as you build them
]

def connect_to_email():
    """Connect to email server"""
    print(f"Connecting to {IMAP_SERVER}...")
    client = IMAPClient(IMAP_SERVER, use_uid=True, ssl=True)
    client.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return client

def get_email_body(email_message):
    """Extract text body from email, handling HTML properly"""
    body = ""
    
    if email_message.is_multipart():
        # Try plain text first
        for part in email_message.walk():
            content_type = part.get_content_type()
            
            if content_type == 'text/plain':
                try:
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    if body.strip():
                        return body
                except:
                    pass
        
        # If no plain text, parse HTML
        for part in email_message.walk():
            content_type = part.get_content_type()
            
            if content_type == 'text/html':
                try:
                    html_body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                    # Use BeautifulSoup to extract text from HTML
                    soup = BeautifulSoup(html_body, 'html.parser')
                    body = soup.get_text(separator='\n', strip=True)
                    return body
                except Exception as e:
                    print(f"Error parsing HTML: {e}")
                    pass
    else:
        try:
            content = email_message.get_payload(decode=True).decode('utf-8', errors='ignore')
            # Check if it's HTML
            if '<html' in content.lower():
                soup = BeautifulSoup(content, 'html.parser')
                body = soup.get_text(separator='\n', strip=True)
            else:
                body = content
        except:
            pass
    
    return body

def process_email(email_id, email_data, client):
    """Process a single email"""
    # Parse email
    msg = BytesParser(policy=policy.default).parsebytes(email_data[b'RFC822'])
    
    sender = msg.get('From', '')
    subject = msg.get('Subject', '')
    body = get_email_body(msg)
    
    print(f"\nProcessing email from: {sender}")
    print(f"Subject: {subject}")
    
    # Try each parser
    for parser in PARSERS:
        if parser.can_parse(sender, subject):
            print(f"Using parser: {parser.__class__.__name__}")
            
            transaction_data = parser.parse(body)
            
            if transaction_data:
                # Send to API
                try:
                    response = requests.post(
                        f"{API_URL}/transactions",
                        params=transaction_data
                    )
                    
                    if response.status_code == 200:
                        print(f"✓ Transaction created: {transaction_data}")
                        # Mark email as seen
                        client.add_flags(email_id, ['\\Seen'])
                        return True
                    else:
                        print(f"✗ API error: {response.status_code}")
                except Exception as e:
                    print(f"✗ Error calling API: {e}")
            else:
                print("✗ Failed to parse transaction")
            
            return False
    
    print("✗ No parser found for this email")
    return False

def check_emails():
    """Check for new bank alerts and process them"""
    try:
        client = connect_to_email()
        client.select_folder('INBOX')
        
        # Search for unread emails
        messages = client.search(['UNSEEN'])
        
        print(f"\nFound {len(messages)} unread emails")
        
        for email_id in messages:
            email_data = client.fetch([email_id], ['RFC822'])
            process_email(email_id, email_data[email_id], client)
        
        client.logout()
        
    except Exception as e:
        print(f"Error checking emails: {e}")

def main():
    """Main loop - check emails periodically"""
    print("Starting email ingestion service...")
    print(f"Checking {EMAIL_ADDRESS} every 60 seconds")
    
    while True:
        check_emails()
        print("\nWaiting 60 seconds before next check...")
        time.sleep(60)

if __name__ == "__main__":
    main()