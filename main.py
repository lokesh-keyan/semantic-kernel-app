import asyncio
from config import load_env_vars
from function_invoke import summarize_text, translate_text
from function_setup import add_summarize_function, add_translator_function
from kernal_setup import create_kernel

def main():
    load_env_vars()
    kernel = create_kernel()
    summarize_fn = add_summarize_function(kernel)
    translate_fn = add_translator_function(kernel)

    text_to_summarize = """
    Semantic Kernel is a lightweight, open-source development kit that lets 
    you easily build AI agents and integrate the latest AI models into your C#, 
    Python, or Java codebase. It serves as an efficient middleware that enables 
    rapid delivery of enterprise-grade solutions.
    """

    text_to_translate = """
    Semantic Kernel is a lightweight, open-source development kit that lets 
    you easily build AI agents and integrate the latest AI models into your C#, 
    Python, or Java codebase. It serves as an efficient middleware that enables 
    rapid delivery of enterprise-grade solutions.
    """

    asyncio.run(summarize_text(kernel, summarize_fn, text_to_summarize))
    asyncio.run(translate_text(kernel, translate_fn, text_to_translate))

if __name__ == "__main__":
    main()