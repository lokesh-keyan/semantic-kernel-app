from config.env_loader import load_env_vars
import asyncio
from config.kernal_config import create_kernel
from functions.setup import add_all_functions
from orchestrator import SemanticOrchestrator

def main():
    load_env_vars()
    kernel = create_kernel()
    functions = add_all_functions(kernel)

    orchestrator = SemanticOrchestrator(kernel, functions)

    text = """
    Semantic Kernel is a lightweight, open-source development kit that lets 
    you easily build AI agents and integrate the latest AI models into your C#, 
    Python, or Java codebase. It serves as an efficient middleware that enables 
    rapid delivery of enterprise-grade solutions.
    """

    asyncio.run(orchestrator.run_all(text))

if __name__ == "__main__":
    main()
