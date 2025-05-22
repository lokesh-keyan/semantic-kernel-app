from semantic_kernel.agents import ChatHistoryAgentThread
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent

async def multi_turn_agent_example():
    simple_agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="ai_assistant",
        instructions="You are an AI assistant that helps users with their questions."
    )

    thread: ChatHistoryAgentThread = None

    user_messages = [
        "hello",
        "Which country has Paris as the capital?",
        "What are its neighboring countries, give a short one-liner list please?",
        ]

    for user_message in user_messages:
        print("*** User:", user_message)
        
        # get our response from the agent
        response = await simple_agent.get_response(messages=user_message, thread=thread)
        print("*** Agent:", response.content)
        
        # save the thread with all the existing messages and responses
        thread = response.thread

    # print the final conversation, so we can see what happens in thread
    print("-" * 25)
    async for m in thread.get_messages():
        print(m.role, m.content)