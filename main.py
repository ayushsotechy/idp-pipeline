import sys
import os
from src.extractor import InvoiceExtractor

def main():
    # 1. Setup the path to your test file
    # Make sure you put a file named 'invoice_sample.pdf' in the data folder!
    pdf_path = "data/invoice_sample.pdf"

    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found at {pdf_path}")
        print("Please put a PDF invoice in the 'data' folder and rename it to 'invoice_sample.pdf'")
        return

    # 2. Run the Extractor
    print(f"🚀 Starting extraction for: {pdf_path}")
    extractor = InvoiceExtractor()
    
    try:
        result = extractor.extract(pdf_path)

        # 3. Print Results
        print("\n✅ SUCCESS! Extracted Data:")
        print("="*40)
        print(f"Vendor:   {result.vendor_name}")
        print(f"Date:     {result.date}")
        print(f"Total:    {result.currency} {result.grand_total}")
        print("-" * 20)
        for item in result.items:
            print(f" • {item.description} (Qty: {item.quantity}) - {item.total_price}")
        print("="*40)

    except Exception as e:
        print(f"\n❌ FAILED: {e}")

if __name__ == "__main__":
    main()