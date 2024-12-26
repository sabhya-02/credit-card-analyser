import os
from parsers.pdf_parser_abstract import PdfParser
from pypdf import PdfReader
import pandas as pd


class SbiParser(PdfParser):
    def __init__(self, statement_folder):
        self.key = self.get_decrypt_key()
        self.statement_folder = statement_folder

    def get_decrypt_key(self) -> str:
        return os.environ["SBI_KEY"]

    def read_card_statement(self) -> pd.DataFrame:
        file_name = os.path.join(self.statement_folder, "SBI.pdf")
        reader = PdfReader(stream=file_name, password=self.get_decrypt_key())
        for page in reader.pages:
            print(f"Page No: {page.page_number}")
            print(page.extract_text())
            print("-" * 50)

    def clean_statement_text(self, text):
        return super().clean_statement_text(text)
