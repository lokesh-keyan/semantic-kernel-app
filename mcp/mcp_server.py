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