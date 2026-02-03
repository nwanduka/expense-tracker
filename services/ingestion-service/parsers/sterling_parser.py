from .base_parser import BankParser
import re
from datetime import datetime

class SterlingBankParser(BankParser):
    """Parser for Sterling Bank transaction alerts"""
    
    def can_parse(self, sender: str, subject: str) -> bool:
        """Check if email is from Sterling Bank"""
        return 'sterling.ng' in sender.lower() or 'money in!' in subject.lower() or 'money out!' in subject.lower()
    
    def parse(self, email_body: str) -> dict:
        """Extract transaction from Sterling Bank alert"""
        try:
            # Extract amount
            amount = self.extract_amount(email_body)
            if not amount:
                print("Could not extract amount")
                return None
            
            # Check transaction type
            transaction_type = self.extract_transaction_type(email_body)
            if transaction_type == 'DEBIT':
                amount = -amount  # Make debits negative
            
            # Extract description
            description = self.extract_description(email_body)
            
            # Extract date
            date = self.extract_date(email_body)
            
            return {
                'amount': amount,
                'description': description,
                'date': date
            }
        except Exception as e:
            print(f"Error parsing Sterling email: {e}")
            return None
    
    def extract_amount(self, text: str) -> float:
        """Extract amount from Sterling alert"""

        # Sterling format: "Amount NGN71,799.99"
        pattern = r'Amount\s+NGN([\d,]+\.?\d*)'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            amount_str = match.group(1).replace(',', '')
            return float(amount_str)
        
        return None
    
    def extract_transaction_type(self, text: str) -> str:
        """Extract transaction type (CREDIT or DEBIT)"""
        # Sterling format: "Transaction CREDIT" or "Transaction DEBIT"
        pattern = r'Transaction\s+(CREDIT|DEBIT)'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            return match.group(1).upper()
        
        return 'DEBIT'  # Default to debit if not found
    
    def extract_description(self, text: str) -> str:
        """Extract transaction description"""
        # Sterling format: "Description [text here]"
        pattern = r'Description\s+(.+?)(?=\s+Amount|\n\n|\Z)'
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        
        if match:
            description = match.group(1).strip()
            # Clean up the description - remove extra whitespace
            description = ' '.join(description.split())
            return description
        
        return "Sterling Bank transaction"
    
    def extract_date(self, text: str) -> str:
        """Extract transaction date"""
        # Sterling format: "Date 03/02/2026 11:31 AM"
        pattern = r'Date\s+(\d{2}/\d{2}/\d{4}\s+\d{1,2}:\d{2}\s+[AP]M)'
        match = re.search(pattern, text, re.IGNORECASE)
        
        if match:
            date_str = match.group(1)
            try:
                # Parse Sterling's date format
                dt = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
                return dt.isoformat()
            except:
                pass
        
        # Fallback to current time
        return datetime.now().isoformat()