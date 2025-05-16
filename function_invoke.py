

async def summarize_text(kernel, summary_fn, text: str):
    """Invoke the summarization semantic function asynchronously."""
    summary = await kernel.invoke(summary_fn, input=text)
    print("Summary:")
    print(summary)

async def translate_text(kernel, translate_fn, text: str, target_lang: str = "French"):
    """Invoke the summarization semantic function asynchronously."""
    translated_text = await kernel.invoke(translate_fn, input=text, target_lang=target_lang)
    print("Translation:")
    print(translated_text)