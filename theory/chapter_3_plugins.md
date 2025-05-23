
# 🧩 Semantic Kernel Plugins Explained

## ✅ What are Plugins in Semantic Kernel?

**Plugins** are named groups of functions your AI agent can call.

These functions can be:
- **Semantic functions**: Powered by LLMs (like GPT-4)
- **Native functions**: Python functions you write

Think of a plugin like a **toolbox** with related tools.

### Example:

| Plugin Name | Functions Inside |
|-------------|------------------|
| `Summarizer` | `tldr` (semantic function) |
| `Translator` | `translate` (semantic function) |
| `Calendar` | `create_event`, `list_events` (native functions) |

---

## 🛠️ How Plugins Work

### 1. Define functions

```python
def add_summarize_function(kernel):
    kernel.add_function(
        plugin_name="Summarizer",
        function_name="tldr",
        prompt="{{$input}}\n\nTL;DR:",
        max_tokens=50
    )
```

### 2. Group them under a plugin name

- In the example above, the plugin is called `"Summarizer"`.

### 3. Kernel keeps track of all plugins

```python
kernel.invoke("Summarizer", "tldr", input="your text here")
```

---

## 🤖 Why Plugins Matter

- ✅ **Extensibility** – Add more skills easily
- 🧠 **Function calling** – Models can auto-select functions
- 📦 **Modularity** – Organize functions cleanly

---

## 🧠 Real-World Example

A travel assistant could have:

- `WeatherPlugin`: `get_weather_forecast`
- `FlightPlugin`: `search_flights`, `book_flight`
- `TranslatorPlugin`: `translate_to`

You or the model can now invoke these by name.

---

## 🚀 Summary

| Concept | Meaning |
|--------|---------|
| **Plugin** | Group of related functions (semantic or native) |
| **Why?** | Organization, reuse, auto function calling |
| **How?** | Register functions with `plugin_name` using the kernel |
| **Use Case** | Agents, chatbots, LLM tools, assistants |
