import pandas as pd
import os
from .extract import extract
from .transform import transform
from .load import load

class ETLPipeline:
    def __init__(self, file_input: str, file_output: str):
        self.file_input = file_input
        self.file_output = file_output
        self.df = None

    def run(self):
        try:
            self.extract()
            self.transform()
            self.load()
        except Exception as e:
            raise RuntimeError(f"ETL ERROR : {e}")

    def extract(self):
        print("📥 Extracting data...")
        self.df = extract(self.file_input)

    def transform(self):
        print("🔁 Transforming data...")
        self.df = transform(self.df)

    def load(self):
        print("📤 Loading data...")
        load(self.df, self.file_output)

