from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.functions.kernel_arguments import KernelArguments

async def simple_agent_example():
    """
    Example of a simple agent using AzureChatCompletion.
    """
    # Initialize the agent with AzureChatCompletion
    simple_agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="ai_assistant",
        instructions="You are an AI assistant that helps users with their questions."
    )

    response = await simple_agent.get_response(messages="What's the capital of France?")
    print("Agent:", response.content)