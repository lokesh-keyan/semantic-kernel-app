# This file has been originally authored by https://github.com/microsoft/OpenAIWorkshop/tree/main/agentic_ai/backend_services

from fastmcp import FastMCP  
from typing import List, Optional, Dict, Any  
from pydantic import BaseModel, Field  
import sqlite3, os, json, math, asyncio, logging  
from datetime import datetime  
from dotenv import load_dotenv  

load_dotenv()

mcp = FastMCP(
    name="Contoso Customer API as Tools",  
    instructions=(
        "All customer, billing and knowledge data is accessible ONLY via the declared "  
        "tools below.  Return values follow the pydantic schemas Always call the most "  
        "specific tool that answers the user’s question."  
    ),  
)

DB_PATH = "contoso.db"
  
def get_db() -> sqlite3.Connection:
    db = sqlite3.connect(DB_PATH)  
    db.row_factory = sqlite3.Row
    return db
  
# — safe OpenAI import / dummy embedding  
try:  
    from openai import AzureOpenAI  
  
    _client = AzureOpenAI(  
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),  
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),  
    )  
    _emb_model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")   #Check what this is set to in your .env file, e.g. "text-embedding-3-small" or "text-embedding-3-large"
  
    def get_embedding(text: str) -> List[float]:
        text = text.replace("\n", " ")
        return _client.embeddings.create(input=[text], model=_emb_model).data[0].embedding
  
except Exception:  # pragma: no cover  
    def get_embedding(text: str) -> List[float]:  
        # 1536‑d zero vector falls back when creds are missing (tests/dev mode)  
        return [0.0] * 1536
  
  
def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

##############################################################################  
#                              Pydantic MODELS                               #  
##############################################################################  
class CustomerSummary(BaseModel):  
    customer_id: int  
    first_name: str  
    last_name: str  
    email: str  
    loyalty_level: str  
  
  
class CustomerDetail(BaseModel):  
    customer_id: int  
    first_name: str  
    last_name: str  
    email: str  
    phone: Optional[str]  
    address: Optional[str]  
    loyalty_level: str  
    subscriptions: List[dict]  
  
  
class Payment(BaseModel):  
    payment_id: int  
    payment_date: Optional[str]  
    amount: float  
    method: str  
    status: str  
  
  
class Invoice(BaseModel):  
    invoice_id: int  
    invoice_date: str  
    amount: float  
    description: str  
    due_date: str  
    payments: List[Payment]  
    outstanding: float

class ServiceIncident(BaseModel):  
    incident_id: int  
    incident_date: str  
    description: str  
    resolution_status: str  
  
  
class SubscriptionDetail(BaseModel):  
    subscription_id: int  
    product_id: int  
    start_date: str  
    end_date: str  
    status: str  
    roaming_enabled: int  
    service_status: str  
    speed_tier: Optional[str]  
    data_cap_gb: Optional[int]  
    autopay_enabled: int  
    product_name: str  
    product_description: Optional[str]  
    category: Optional[str]  
    monthly_fee: Optional[float]  
    invoices: List[Invoice]  
    service_incidents: List[ServiceIncident]  
  
  
class Promotion(BaseModel):  
    promotion_id: int  
    product_id: int  
    name: str  
    description: str  
    eligibility_criteria: Optional[str]  
    start_date: str  
    end_date: str  
    discount_percent: Optional[int]

class KBSearchParams(BaseModel):  
    query: str = Field(..., description="natural language query")  
    topk: Optional[int] = Field(3, description="Number of top documents to return")  
  
  
class KBDoc(BaseModel):  
    title: str  
    doc_type: str  
    content: str  
  
  
class SecurityLog(BaseModel):  
    log_id: int  
    event_type: str  
    event_timestamp: str  
    description: str  
  
  
class Order(BaseModel):  
    order_id: int  
    order_date: str  
    product_name: str  
    amount: float  
    order_status: str  
  
  
class DataUsageRecord(BaseModel):  
    usage_date: str  
    data_used_mb: int  
    voice_minutes: int  
    sms_count: int  

class SupportTicket(BaseModel):  
    ticket_id: int  
    subscription_id: int  
    category: str  
    opened_at: str  
    closed_at: Optional[str]  
    status: str  
    priority: str  
    subject: str  
    description: str  
    cs_agent: str  
  
  
class SubscriptionUpdateRequest(BaseModel):  
    roaming_enabled: Optional[int] = None  
    status: Optional[str] = None  
    service_status: Optional[str] = None  
    product_id: Optional[int] = None  
    start_date: Optional[str] = None  
    end_date: Optional[str] = None  
    autopay_enabled: Optional[int] = None  
    speed_tier: Optional[str] = None  
    data_cap_gb: Optional[int] = None  
  
  
# ─── simple arg models ───────────────────────────────────────────────────  
class CustomerIdParam(BaseModel):  
    customer_id: int  
  
  
class SubscriptionIdParam(BaseModel):  
    subscription_id: int  
  
  
class InvoiceIdParam(BaseModel):  
    invoice_id: int  


@mcp.tool(description="List all customers with basic info")  
def get_all_customers() -> List[CustomerSummary]:  
    db = get_db()  
    rows = db.execute(  
        "SELECT customer_id, first_name, last_name, email, loyalty_level FROM Customers"  
    ).fetchall()  
    db.close()  
    return [CustomerSummary(**dict(r)) for r in rows]  
  
  
@mcp.tool(description="Get a full customer profile including their subscriptions")  
def get_customer_detail(params: CustomerIdParam) -> CustomerDetail:  
    db = get_db()  
    cust = db.execute(  
        "SELECT * FROM Customers WHERE customer_id = ?", (params.customer_id,)  
    ).fetchone()  
    if not cust:  
        db.close()  
        raise ValueError(f"Customer {params.customer_id} not found")  
    subs = db.execute(  
        "SELECT * FROM Subscriptions WHERE customer_id = ?", (params.customer_id,)  
    ).fetchall()  
    db.close()  
    return CustomerDetail(**dict(cust), subscriptions=[dict(s) for s in subs])  