from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent

def generate_specialized_agent(expertise, tone, length):
    templated_agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name=f"{expertise}_assistant",
        instructions="""You are an AI assistant specializing in {{$expertise}}.
        Your tone should be {{$tone}} and your responses should be {{$length}} in length.
        """,
        arguments=KernelArguments(
            expertise=expertise,
            tone=tone,
            length=length
        ),
    )
    return templated_agent

async def specialized_agent_example():
    """
    Example of a specialized agent using AzureChatCompletion.
    """
    python_agent = generate_specialized_agent("python_programming", "friendly", "short")
    java_agent = generate_specialized_agent("java_programming", "funny and snappy", "short")

    print("Python agent:\n", await python_agent.get_response(messages="Write me a hello world example"))
    print("Java agent:\n",await java_agent.get_response(messages="Write me a hello world example"))
