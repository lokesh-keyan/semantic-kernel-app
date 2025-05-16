# Getting Started with Azure OpenAI + Semantic Kernel

## 🚀 Step 1: Set Up Azure OpenAI Resource

1. Go to the [Azure Portal](https://portal.azure.com/)
2. Search for **Azure OpenAI** and click **Create**
3. Fill in the required details:
   - **Subscription**: Select your Azure subscription
   - **Resource Group**: Use an existing one or create a new one
   - **Region**: Choose a supported region (e.g., *East US*, *West Europe*)
   - **Name**: Give your Azure OpenAI resource a unique name
4. Click **Review + Create**, then **Create**

---

## 🌐 Step 2: Access Azure AI Studio

1. Navigate to the **Overview** tab of your Azure OpenAI resource
2. Click **Get Started**
3. Click **Explore Azure AI Foundry Portal**
4. Inside the portal, create a **Deployment** (e.g., `gpt-35-turbo`, or your preferred model)

---

## 🛠 Step 3: Set Up Local Project

### 1. Create a Project Folder

```bash
mkdir my-ai-project
cd my-ai-project
code .
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
.venv/Scripts/activate.ps1  # For PowerShell (Windows)
```

### 3. Install Semantic Kernel

```bash
pip install semantic-kernel
```

---

## 🔐 Step 4: Create and Configure `.env` File

Create a `.env` file in the root of your project with the following content:

```env
AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_API_VERSION=2025-03-01-preview
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=gpt-4o-2024-11-20
```

---

## 🧠 Step 5: Kernel Setup

Create a `kernel_setup.py` file:

```python
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

def create_kernel() -> Kernel:
    """Initialize the kernel and add Azure Chat Completion service."""
    kernel = Kernel()
    chat_completion = AzureChatCompletion()
    kernel.add_service(chat_completion)
    return kernel
```

This automatically pulls config from your `.env`.

---

## 🧪 Step 6: Add Semantic Functions

### TL;DR Summary Function

```python
prompt_template = "{{$input}}\n\nTL;DR in one sentence:"

summarize_fn = kernel.add_function(
    prompt=prompt_template,
    function_name="tldr",
    plugin_name="Summarizer",
    max_tokens=50,
)

long_text = """
Semantic Kernel is a lightweight, open-source development kit that lets 
you easily build AI agents and integrate the latest AI models into your C#, 
Python, or Java codebase. It serves as an efficient middleware that enables 
rapid delivery of enterprise-grade solutions.
"""

summary = await kernel.invoke(summarize_fn, input=long_text)
print(summary)
```

---

### Translation Function

```python
prompt_template = "{{$input}}\n\nTranslate this into {{$target_lang}}:"

translate_fn = kernel.add_function(
    prompt=prompt_template, 
    function_name="translator", 
    plugin_name="Translator",
    max_tokens=50)

text = """
Semantic Kernel is a lightweight, open-source development kit that lets 
you easily build AI agents and integrate the latest AI models into your C#, 
Python, or Java codebase. It serves as an efficient middleware that enables 
rapid delivery of enterprise-grade solutions.
"""

translated = await kernel.invoke(translate_fn, input=text, target_lang="French")
print(translated)
```

---

## ✅ Done!

You now have:
- Azure OpenAI setup
- A project folder with semantic kernel installed
- Environment config loading from `.env`
- Working summarization and translation functions 🎉