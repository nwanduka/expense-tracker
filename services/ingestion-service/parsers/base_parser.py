from abc import ABC, abstractmethod
import re

class BankParser(ABC):
    """Base class for all bank parsers"""
    
    @abstractmethod
    def can_parse(self, sender: str, subject: str) -> bool:
        """
        Check if this parser can handle the email
        Returns True if this parser should process this email
        """
        pass
    
    @abstractmethod
    def parse(self, email_body: str) -> dict:
        """
        Extract transaction details from email body
        Returns dict with: amount, description, date
        Returns None if parsing fails
        """
        pass
    
    def extract_amount(self, text: str) -> float:
        """Helper to extract amount from text"""
        # Look for patterns like: NGN 5,000.00 or N5000 or 5000.00
        patterns = [
            r'NGN\s*([\d,]+\.?\d*)',
            r'N([\d,]+\.?\d*)',
            r'Amount:\s*([\d,]+\.?\d*)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                amount_str = match.group(1).replace(',', '')
                return float(amount_str)
        
        return None