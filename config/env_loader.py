import os
from dotenv import load_dotenv

def load_env_vars() -> None:
    """Load and validate required environment variables."""
    load_dotenv()

    required_vars = ["AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "AZURE_OPENAI_API_KEY"]
    missing = [var for var in required_vars if not os.getenv(var)]
    if missing:
        raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")