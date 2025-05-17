# Semantic Kernel Azure Setup Instructions

## ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/lokesh-keyan/semantic-kernal-app.git
cd semantic-kernal-app
```

## ✅ Step 2: Install Dependencies

Make sure you're in a virtual environment, then run:

```bash
pip install -r requirements.txt
```

## ✅ Step 3: Set Up Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Update `.env` with your Azure OpenAI and Azure AI Foundary configuration:

```
AZURE_OPENAI_ENDPOINT=https://xxxxxx.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_KEY=xxxxxxxxxxx
AZURE_OPENAI_API_VERSION=2025-03-01-preview
```

> Replace `xxxxxx` and `xxxxxxxxxxx` with your actual Azure OpenAI resource details.

## ✅ Step 4: Run the Application

```bash
python main.py
```

This will execute the main program and demonstrate how the Semantic Kernel works with Azure OpenAI.

---

Happy hacking! 🚀
