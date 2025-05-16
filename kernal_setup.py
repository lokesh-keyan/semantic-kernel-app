# kernel_setup.py
from semantic_kernel.kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

def create_kernel() -> Kernel:
    """Initialize the kernel and add Azure Chat Completion service."""
    kernel = Kernel()
    chat_completion = AzureChatCompletion()
    kernel.add_service(chat_completion)
    return kernel