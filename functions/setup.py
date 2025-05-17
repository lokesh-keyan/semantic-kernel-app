from semantic_kernel import Kernel

def add_semantic_function(kernel: Kernel, plugin_name: str, function_name: str, prompt_template: str, max_tokens: int = 50):
    return kernel.add_function(
        prompt=prompt_template,
        function_name=function_name,
        plugin_name=plugin_name, # all summarization-related functions can be under "Summarizer". Grouping functions are plugins
        max_tokens=max_tokens,
    )

def add_summarize_function(kernel: Kernel):
    prompt = "{{$input}}\n\nTL;DR in one sentence:"
    return add_semantic_function(kernel, "Summarizer", "tldr", prompt)

def add_translator_function(kernel: Kernel):
    prompt = "{{$input}}\n\nTranslate this into {{$target_lang}}:"
    return add_semantic_function(kernel, "Translator", "translator", prompt)

def add_all_functions(kernel: Kernel):
    return {
        "tldr": add_summarize_function(kernel),
        "translator": add_translator_function(kernel),
        # Add more here as needed
    }