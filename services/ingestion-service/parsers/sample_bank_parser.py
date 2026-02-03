from .base_parser import BankParser
import re
from datetime import datetime

class SampleBankParser(BankParser):
    """Parser for Sample Bank transaction alerts"""
    
    def can_parse(self, sender: str, subject: str) -> bool:
        """Check if email is from Sample Bank"""
        # Customize this with your bank's email domain
        return 'samplebank.com' in sender.lower() or 'transaction alert' in subject.lower()
    
    def parse(self, email_body: str) -> dict:
        """Extract transaction from Sample Bank alert"""
        try:
            # Extract amount
            amount = self.extract_amount(email_body)
            if not amount:
                return None
            
            # Determine if it's debit or credit
            is_debit = 'debit' in email_body.lower() or 'withdrawal' in email_body.lower()
            if is_debit:
                amount = -amount  # Make debits negative
            
            # Extract description
            description = self.extract_description(email_body)
            
            return {
                'amount': amount,
                'description': description,
                'date': datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error parsing email: {e}")
            return None
    
    def extract_description(self, text: str) -> str:
        """Extract transaction description"""
        # Look for common patterns in transaction alerts
        patterns = [
            r'Description:\s*(.+?)(?:\n|$)',
            r'Narration:\s*(.+?)(?:\n|$)',
            r'Details:\s*(.+?)(?:\n|$)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # Fallback: generic description
        return "Transaction from email alert"