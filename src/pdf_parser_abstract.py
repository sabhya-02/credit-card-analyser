from abc import ABC, abstractmethod
import pandas as pd 
class PdfParser(ABC):
    def __init__(self):
        """
        Abstract class to read credit card statement
        """
        pass
    @abstractmethod
    def decrypt(self):
        """
        Decrypt the card statement
        """
        pass
    @abstractmethod
    def read_card_statement(self, file_path: str) -> str:
        """
        Reads the pdf file at file_path and returns the text
        """
        pass
    @abstractmethod
    def clean_statement_text(self, text) -> pd.DataFrame:
        """
        Cleans the statement and return the line items in a DataFrame
        """
        pass
