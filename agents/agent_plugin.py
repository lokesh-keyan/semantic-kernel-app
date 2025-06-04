from datetime import datetime
from typing import Annotated, List, Tuple
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.functions import kernel_function

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

async def notes_agent_example():
    """
    Example of an agent using a plugin to manage notes.
    """
    # Initialize the agent with AzureChatCompletion and the NotesPlugin
    agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="notes_assistant",
        instructions="You are a helpful assistant.",
        plugins=[NotesPlugin()],
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