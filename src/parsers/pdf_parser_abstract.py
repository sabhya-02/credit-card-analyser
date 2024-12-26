from abc import ABC, abstractmethod
import pandas as pd


class PdfParser(ABC):
    def __init__(self):
        """
        Abstract class to read credit card statement
        """
        pass

    def get_decrypt_key(self) -> str:
        """
        Get the key to decrypt the PDF File
        """
        pass

    @abstractmethod
    def read_card_statement(self, file_path: str) -> str:
        """
        Reads the pdf file at file_path and returns the text
        """
        pass

    @abstractmethod
    def clean_statement_text(self, text: str) -> pd.DataFrame:
        """
        Cleans the statement and return the line items in a DataFrame
        """
        pass
