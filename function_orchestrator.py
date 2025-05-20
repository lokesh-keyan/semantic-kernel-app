import asyncio

class SemanticOrchestrator:
    def __init__(self, kernel, functions):
        self.kernel = kernel
        self.functions = functions

    async def summarize(self, text: str):
        summary = await self.kernel.invoke(self.functions["tldr"], input=text)
        print("Summary:")
        print(summary)
        return summary

    async def translate(self, text: str, target_lang: str = "French"):
        translation = await self.kernel.invoke(self.functions["translator"], input=text, target_lang=target_lang)
        print("Translation:")
        print(translation)
        return translation

    async def run_all(self, text: str):
        await self.summarize(text)
        await self.translate(text)
