from agents.multi_turn_agent import multi_turn_agent_example
from agents.simple_agent import simple_agent_example
from agents.specialized_agent import specialized_agent_example
from config.env_loader import load_env_vars
import asyncio
from config.kernal_config import create_kernel
from functions.setup import add_all_functions
from function_orchestrator import SemanticOrchestrator
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

from plugin_orchestrator import run_weather_report_plugin

def main():
    load_env_vars()
    # chat_completion = AzureChatCompletion()
    # kernel = create_kernel(chat_completion)
    # functions = add_all_functions(kernel)

    # # Run the functions individually
    # orchestrator = SemanticOrchestrator(kernel, functions)
    # text = """
    # Semantic Kernel is a lightweight, open-source development kit that lets 
    # you easily build AI agents and integrate the latest AI models into your C#, 
    # Python, or Java codebase. It serves as an efficient middleware that enables 
    # rapid delivery of enterprise-grade solutions
    # """
    # asyncio.run(orchestrator.run_all(text))

    # # Run the weather report plugin
    # user_message = "What's the weather like in Tokyo and are there any alerts?"
    # asyncio.run(run_weather_report_plugin(kernel, chat_completion, user_message))

    # asyncio.run(simple_agent_example())

    # asyncio.run(specialized_agent_example())
    asyncio.run(multi_turn_agent_example())

if __name__ == "__main__":
    main()
