from semantic_kernel.contents import ChatHistorySummarizationReducer
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.agents import ChatHistoryAgentThread

async def keeping_length_in_check_example():
    chat_history_with_reducer = ChatHistorySummarizationReducer(
    service=AzureChatCompletion(),
    target_count=2,
    threshold_count=2,
    )
    chat_history_with_reducer.clear()

    simple_agent = ChatCompletionAgent(
        service=AzureChatCompletion(),
        name="ai_assistant",
        instructions="You are an AI assistant that returns the numbers the user gives you."
    )

    thread: ChatHistoryAgentThread = ChatHistoryAgentThread(chat_history=chat_history_with_reducer)

    for i in range(10):
        user_message = f"hello {i}, please return this number!"
        print("*** User:", user_message)
        response = await simple_agent.get_response(messages=user_message, thread=thread)
        thread = response.thread
        print("*** Agent:", response.content)
        
        print(f"--> Message Count: {len(thread)}")
        # Manually trigger the reduction, but we can also set it to auto on ChatHistorySummarizationReducer
        is_reduced = await thread.reduce()
        if is_reduced:
            print(f"--> History reduced to {len(thread)} messages.")
            # print summary
            async for msg in thread.get_messages():
                if msg.metadata and msg.metadata.get("__summary__"):
                    print(f"--> Summary: {msg.content}")
                    break



    # print the final conversation, so we can see what happens in thread
    print("-" * 10)
    async for m in thread.get_messages():
        print(m.role, m.content)