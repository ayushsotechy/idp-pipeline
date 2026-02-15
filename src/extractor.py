from google import genai
from google.genai import types
from src.config import settings
from src.models import InvoiceData
import os

class InvoiceExtractor:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def extract(self, file_path: str) -> InvoiceData:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        print(f"Processing file: {file_path}")
        
        # 1. Upload
        file_upload = self.client.files.upload(file=file_path)

        # 2. Generate
        response = self.client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=[
                file_upload,
                "Extract the data from this invoice perfectly."
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=InvoiceData
            )
        )
        return response.parsed