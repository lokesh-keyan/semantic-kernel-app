from config.env_loader import load_env_vars
import asyncio
from config.kernal_config import create_kernel
from functions.setup import add_all_functions
from function_orchestrator import SemanticOrchestrator
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from plugin_orchestrator import run_weather_report_plugin

def main():
    load_env_vars()
    chat_completion = AzureChatCompletion()
    kernel = create_kernel(chat_completion)
    functions = add_all_functions(kernel)

    orchestrator = SemanticOrchestrator(kernel, functions)

    text = """
    Semantic Kernel is a lightweight, open-source development kit that lets 
    you easily build AI agents and integrate the latest AI models into your C#, 
    Python, or Java codebase. It serves as an efficient middleware that enables 
    rapid delivery of enterprise-grade solutions
    """
    # Run the functions individually
    asyncio.run(orchestrator.run_all(text))

    # Run the weather report plugin
    asyncio.run(run_weather_report_plugin(kernel, chat_completion))



if __name__ == "__main__":
    main()
