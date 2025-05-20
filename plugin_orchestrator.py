from semantic_kernel import Kernel
from plugins.weather_plugin import WeatherPlugin
from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior,
)
from semantic_kernel.contents.chat_history import ChatHistory

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

async def run_weather_report_plugin(kernel: Kernel, chat_completion: AzureChatCompletion):
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

    result = await chat_completion.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=kernel,
    )

    print("Assistant > " + str(result))