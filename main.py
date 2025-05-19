from config.env_loader import load_env_vars
import asyncio
from config.kernal_config import create_kernel
from functions.setup import add_all_functions
from orchestrator import SemanticOrchestrator
from plugins.weather_plugin import WeatherPlugin
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior,
)
from semantic_kernel.contents.chat_history import ChatHistory

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)

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

    # Usage example:
    # Create the plugin
    weather_plugin = WeatherPlugin()

    # Register with kernel
    kernel.add_plugin(
        plugin=weather_plugin,
        plugin_name="Weather"
    )

    # Test with a user query
    history = ChatHistory()
    history.add_user_message("What's the weather like in Tokyo and are there any alerts?")

    # Get response using function calling
    execution_settings = AzureChatPromptExecutionSettings()

    #FunctionChoiceBehavior.Auto() tells the model:
    #“When you think one of the available functions is relevant based on the user's prompt, automatically call it.”
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    result = asyncio.run(chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=kernel,
    ))

    print("Assistant > " + str(result))

if __name__ == "__main__":
    main()
