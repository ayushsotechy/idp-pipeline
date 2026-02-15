from fastapi import FastAPI, UploadFile, File, HTTPException
from src.extractor import InvoiceExtractor
from src.models import InvoiceData
import shutil
import os

app = FastAPI(title="Invoice Extraction API")

# Initialize our AI worker
extractor = InvoiceExtractor()

@app.post("/extract", response_model=InvoiceData)
async def extract_invoice(file: UploadFile = File(...)):
    """
    Upload a PDF/Image invoice and get structured JSON back.
    """
    # 1. Save the uploaded file temporarily
    temp_filename = f"temp_{file.filename}"
    
    try:
        with open(temp_filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # 2. Run the extraction
        result = extractor.extract(temp_filename)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # 3. Cleanup: Delete the temp file so your server doesn't explode
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

@app.get("/")
def home():
    return {"message": "IDP Pipeline is Running! Go to /docs to test."}