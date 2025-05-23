
# Semantic Kernel: Functions and Plugins Explained

## What is Semantic Kernel?

Semantic Kernel (SK) is a framework that helps developers build AI-powered applications by orchestrating large language models (LLMs) alongside traditional code and external services.

---

## Functions in Semantic Kernel

Functions are reusable units of logic — the building blocks in SK.

### Two Types of Functions:

1. **Native Functions**  
   - Regular code methods (e.g., C#, Python) callable by SK.  
   - Examples: reading a file, sending an email, calling a database.

2. **Semantic Functions**  
   - Powered by LLM prompts.  
   - You provide a prompt template, SK generates text via the LLM.  
   - Examples: summarize text, translate language, generate code.

### How They Work Together:

- Functions can be called sequentially or combined in pipelines.  
- Outputs of one function can feed into another.  
- Functions can interact with the LLM or external APIs.

---

## Plugins in Semantic Kernel

Plugins are collections of related functions grouped as **skills**.

- They package multiple functions to provide a domain-specific capability.  
- They can be shared and reused across applications.

### Example Plugins:

- **Weather plugin**: functions like `GetCurrentWeather`, `GetForecast`.  
- **Calendar plugin**: functions like `CreateEvent`, `ListEvents`.  
- **Text processing plugin**: semantic functions to summarize or translate.

---

## Summary

| Concept    | Description                             | Example                                  |
|------------|---------------------------------------|------------------------------------------|
| Function   | Single reusable logic unit             | Semantic: Generate summary<br>Native: Call REST API |
| Plugin     | Group of related functions (a skill)  | Weather plugin with multiple weather functions |

---

## Why Use Functions and Plugins?

- Modularize AI and non-AI logic with functions.  
- Organize capabilities into reusable plugins.  
- Build complex AI apps easily and maintainably.

---
