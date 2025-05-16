from semantic_kernel import Kernel

def add_summarize_function(kernel: Kernel):
    """Add the TL;DR semantic function to the kernel."""
    prompt_template = "{{$input}}\n\nTL;DR in one sentence:"
    return kernel.add_function(
        prompt=prompt_template,
        function_name="tldr",
        plugin_name="Summarizer",
        max_tokens=50,
    )

def add_translator_function(kernel: Kernel):
    """Add the TL;DR semantic function to the kernel."""
    prompt_template = "{{$input}}\n\nTranslate this into {{$target_lang}}:"
    return kernel.add_function(
        prompt=prompt_template,
        function_name="translator",
        plugin_name="Translator",
        max_tokens=50,
    )