from pydantic import BaseModel, Field
from typing import List, Optional

# 1. Define the structure of a single line item
class LineItem(BaseModel):
    description: str = Field(description="Name or description of the product/service")
    quantity: int = Field(default=1, description="Count of items")
    unit_price: float = Field(description="Price per unit")
    total_price: float = Field(description="Total line price")

# 2. Define the structure of the entire invoice
class InvoiceData(BaseModel):
    invoice_number: Optional[str] = Field(description="Unique invoice identifier")
    vendor_name: str = Field(description="Company issuing the invoice")
    date: str = Field(description="Invoice date (YYYY-MM-DD)")
    items: List[LineItem] = Field(description="List of line items")
    subtotal: float = Field(description="Subtotal before tax")
    tax_amount: float = Field(description="Total tax amount")
    grand_total: float = Field(description="Final total to be paid")
    currency: str = Field(default="USD", description="Currency code (e.g., USD, INR)")