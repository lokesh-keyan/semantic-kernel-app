from datetime import datetime
from typing import Annotated, List, Tuple
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.functions import kernel_function
from typing import Awaitable, Callable
from semantic_kernel.kernel import Kernel
from semantic_kernel.filters import FilterTypes, FunctionInvocationContext
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import OpenAIChatPromptExecutionSettings
from semantic_kernel.functions import KernelArguments
# older versions
# from semantic_kernel.kernel_arguments import KernelArguments

class NotesPlugin:
    """A simple plugin to manage notes."""

    def __init__(self):
        self.notes = []

    @kernel_function(description="List all saved notes with their timestamps.")
    def list_notes(self) -> Annotated[List[Tuple[str, str]], "Returns all notes as (timestamp, note)."]:
        """Return all notes with their timestamps."""
        return self.notes

    @kernel_function(description="Save a new note with the current timestamp.")
    def write_note(self, note: Annotated[str, "The note message to save."]) -> str:
        """Save a note with the current timestamp."""
        timestamp = datetime.now().isoformat()
        self.notes.append((timestamp, note))
        return f"Note saved at {timestamp}."
    
async def function_invocation_filter(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    # this runs before the function is called
    print(f"  ---> Calling Plugin {context.function.plugin_name}.{context.function.name} with arguments `{context.arguments}`")
    # let's await the function call
    await next(context)
    # this runs after our functions has been called
    print(f"  ---> Plugin response from [{context.function.plugin_name}.{context.function.name} is `{context.result}`")

async def notes_agent_example():
    """
    Example of an agent using a plugin to manage notes.
    """

    kernel = Kernel()
    kernel.add_filter(FilterTypes.FUNCTION_INVOCATION, function_invocation_filter)

    # Auto-invoke (default behavior)
    # Function Calling Modes
    # For now, we didn't really mess with the function calling behavior, but Semantic Kernel supports different modes for function calling:

    # Auto: The agent automatically decides whether to call functions based on the context.
    # RequireFunction: The agent must call at least one function in its response.
    # Disabled: The agent cannot call functions; it must respond using only text.
    settings = OpenAIChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())

    # Initialize the agent with AzureChatCompletion and the NotesPlugin
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        kernel=kernel,
        name="notes_assistant",
        instructions="You are a helpful assistant.",
        plugins=[NotesPlugin()],
        arguments=KernelArguments(settings),
    )

    messages = [
        "I need to buy milk",
        "Remember to buy coffee for my wife",
        "What notes do I have?",
    ]

    # no chat history here, but we might need this in a real-world scenario
    for m in messages:
        print("*** User:", m)
        print("*** Agent:", await agent.get_response(messages=m))