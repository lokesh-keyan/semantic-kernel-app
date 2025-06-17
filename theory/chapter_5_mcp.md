# Chapter 5: Model Context Protocol (MCP)

## What is Model Context Protocol (MCP)?

**Model Context Protocol (MCP)** is an open standard that enables AI models and applications to securely access external data sources and tools in a standardized way. Think of it as a universal translator that allows AI assistants to connect with various services, databases, and APIs without needing custom integrations for each one.

### Key Concepts

- **Standardized Communication**: MCP provides a consistent way for AI models to interact with external resources
- **Security**: Built-in authentication and authorization mechanisms
- **Extensibility**: Easy to add new data sources and tools
- **Interoperability**: Works across different AI platforms and models

## Why Use MCP?

### Before MCP
```
AI Model → Custom Integration → Database
AI Model → Custom Integration → API Service  
AI Model → Custom Integration → File System
AI Model → Custom Integration → Web Service
```
*Each integration required custom code and maintenance*

### With MCP
```
AI Model → MCP Client → MCP Server → Multiple Resources
                                  ├── Database
                                  ├── API Service
                                  ├── File System
                                  └── Web Service
```
*One standardized protocol for all integrations*

## Simple Example: Weather Information Service

Let's create a simple MCP server that provides weather information:

### 1. MCP Server Structure

```python
# weather_mcp_server.py
import json
from typing import Dict, Any, List
from mcp import Server, get_model_context

class WeatherMCPServer:
    def __init__(self):
        self.server = Server("weather-server")
        self.weather_data = {
            "New York": {"temp": 72, "condition": "Sunny", "humidity": 45},
            "London": {"temp": 65, "condition": "Cloudy", "humidity": 70},
            "Tokyo": {"temp": 78, "condition": "Rainy", "humidity": 80}
        }
    
    def get_weather(self, city: str) -> Dict[str, Any]:
        """Get weather information for a specific city"""
        return self.weather_data.get(city, {"error": "City not found"})
    
    def list_cities(self) -> List[str]:
        """List all available cities"""
        return list(self.weather_data.keys())

# Initialize the server
weather_server = WeatherMCPServer()
```

### 2. MCP Client Usage

```python
# weather_client.py
from mcp import Client
import asyncio

async def main():
    # Connect to the MCP server
    client = Client()
    await client.connect("weather-server")
    
    # Use the weather service
    try:
        # Get weather for New York
        weather = await client.call_tool("get_weather", {"city": "New York"})
        print(f"Weather in New York: {weather}")
        
        # List available cities
        cities = await client.call_tool("list_cities", {})
        print(f"Available cities: {cities}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        await client.disconnect()

# Run the client
asyncio.run(main())
```

### 3. AI Model Integration

```python
# ai_weather_assistant.py
import semantic_kernel as sk
from mcp import Client

class WeatherAssistant:
    def __init__(self):
        self.kernel = sk.Kernel()
        self.mcp_client = Client()
    
    async def setup(self):
        """Setup the MCP connection"""
        await self.mcp_client.connect("weather-server")
    
    async def get_weather_info(self, user_query: str):
        """Process user query and get weather information"""
        # Extract city name from user query (simplified)
        city = self.extract_city_name(user_query)
        
        # Get weather data via MCP
        weather_data = await self.mcp_client.call_tool("get_weather", {"city": city})
        
        # Format response
        if "error" not in weather_data:
            return f"The weather in {city} is {weather_data['condition']} with a temperature of {weather_data['temp']}°F and {weather_data['humidity']}% humidity."
        else:
            return f"Sorry, I don't have weather information for {city}."
    
    def extract_city_name(self, query: str) -> str:
        """Simple city extraction (in real scenarios, use NLP)"""
        cities = ["New York", "London", "Tokyo"]
        for city in cities:
            if city.lower() in query.lower():
                return city
        return "Unknown"

# Usage example
async def demo():
    assistant = WeatherAssistant()
    await assistant.setup()
    
    response = await assistant.get_weather_info("What's the weather like in New York?")
    print(response)
    # Output: "The weather in New York is Sunny with a temperature of 72°F and 45% humidity."
```

## Real-World MCP Use Cases

### 1. Database Access
```python
# Database MCP Server
class DatabaseMCPServer:
    def query_customers(self, filter_criteria: dict):
        # Execute database query
        return customers_data
    
    def get_order_history(self, customer_id: str):
        # Retrieve order history
        return order_data
```

### 2. File System Access
```python
# File System MCP Server
class FileSystemMCPServer:
    def read_file(self, file_path: str):
        # Read file content securely
        return file_content
    
    def list_directory(self, directory_path: str):
        # List directory contents
        return file_list
```

### 3. API Integration
```python
# API MCP Server
class APIMCPServer:
    def call_external_api(self, endpoint: str, params: dict):
        # Make secure API calls
        return api_response
    
    def get_user_data(self, user_id: str):
        # Fetch user data from external service
        return user_info
```

## Benefits of Using MCP

### 🔒 **Security**
- Built-in authentication and authorization
- Secure data transmission
- Access control mechanisms

### 🔧 **Standardization**
- Consistent API across different services
- Reduced development time
- Easier maintenance

### 🚀 **Scalability**
- Easy to add new data sources
- Supports multiple concurrent connections
- Efficient resource management

### 🔄 **Flexibility**
- Works with any AI model or platform
- Supports various data formats
- Customizable for specific needs

## Getting Started with MCP

### Step 1: Install MCP Library
```bash
pip install model-context-protocol
```

### Step 2: Create Your First MCP Server
```python
from mcp import Server

server = Server("my-first-server")

@server.tool("hello_world")
def hello_world(name: str = "World"):
    return f"Hello, {name}!"

if __name__ == "__main__":
    server.run()
```

### Step 3: Connect from Your AI Application
```python
from mcp import Client

async def use_mcp():
    client = Client()
    await client.connect("my-first-server")
    
    result = await client.call_tool("hello_world", {"name": "MCP User"})
    print(result)  # Output: "Hello, MCP User!"
```

## Best Practices

1. **Error Handling**: Always implement proper error handling in both server and client
2. **Authentication**: Use secure authentication mechanisms for sensitive data
3. **Rate Limiting**: Implement rate limiting to prevent abuse
4. **Documentation**: Document your MCP tools and their parameters clearly
5. **Testing**: Write comprehensive tests for your MCP implementations

## Conclusion

MCP simplifies the integration between AI models and external data sources by providing a standardized protocol. Instead of building custom integrations for each service, you can use MCP to create reusable, secure, and maintainable connections that work across different AI platforms.

The weather example above demonstrates how MCP can make it easy for AI assistants to access real-time data while maintaining security and standardization principles.

Traditional Approach:
AI Agent → Cache → Stale Data → Poor Decision

MCP Approach:
AI Agent → MCP Server → Live Data → Optimal Decision


Customer Service AI: "Is product X in stock?"
     ↓ (calls MCP)
Inventory MCP Server: "Yes, 15 units available"
     ↓ (simultaneously)
Pricing AI: "Demand is high, increase price by 5%"
Logistics AI: "Schedule restock from Warehouse B"