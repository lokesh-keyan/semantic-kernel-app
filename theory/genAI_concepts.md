
# Understanding LLMs and GPT Models

## Initial Use Cases for GenAI

The initial use cases for GenAI were to generate text based on a simple instruction called a prompt.

The technology used behind most text-based GenAI products is called a **transformer**, introduced in the paper _Attention is All you Need_ (2017). The transformer greatly improved the quality of generated text, making it resemble human writing. It improved the ability of AI to guess masked words in a phrase after being trained on a large number of documents (a **corpus**).

Models trained on very large corpora are called **large language models (LLMs)**.

---

## What Determines the Performance of an LLM?

- **Number of parameters**: Related to how many comparisons the model can make.
- **Context window**: The max size of the text it can handle at once.
- **Training data**: Often kept secret by companies.

---

## Evolution of GPT Models

| Model     | Parameters         | Context Window | Release Date   |
|-----------|--------------------|----------------|----------------|
| GPT-1     | 120 million        | 512 tokens     | Feb 2018       |
| GPT-2     | 1.5 billion        | 1,024 tokens   | Feb 2019       |
| GPT-3     | 175 billion        | 2,048 tokens   | Jun 2020       |
| GPT-3.5   | 175 billion        | 4,096 ➜ 16,384 | Nov 2022       |

---

## What is ChatGPT?

**ChatGPT** is a web/mobile app using GPT models, allowing users to submit prompts and receive responses. Launched with GPT-3.5, it became the fastest-growing consumer product ever (100M users in < 2 months).

---

## What is the Core Component of an LLM?

A **transformer-based neural network** trained to predict the next token based on prior context.

### 🔧 Core Components

1. **Tokenizer**
   - Breaks text into tokens.
   - Example: `"Hello world!"` ➜ `[15496, 995]`

2. **Embedding Layer**
   - Turns tokens into dense numeric vectors.

3. **Transformer Layers**
   - **Self-attention**: Understands important context words.
   - **Feedforward layers**: Models complex patterns.
   - **Layer normalization + residuals**: For stability.

4. **Output Layer**
   - Converts final vectors into probabilities for the next token.

5. **Loss Function (Training Only)**
   - Reduces error between predicted and actual tokens.

---

## ⚙️ How It Works (Example)

Input: `"The sky is"`

### Behind the Scenes:
1. Tokenizer ➜ `[101, 241, 206]`
2. Embeddings ➜ Dense vectors
3. Transformer ➜ Learns context
4. Output ➜ Predicts `"blue"`

The model continues generating tokens until it finishes the sentence.

---

## 🔁 Training

Example training inputs:
- `"The capital of France is ___"`
- `"Once upon a time, there was a ___"`

The model adjusts billions of weights to get better at predictions.

---

## 🛠️ What's Running Behind the LLM?

When using an LLM (like GPT-4), you interact with a **smart service** that:

- Loads the trained model (100GB+ weights)
- Runs inference on high-end GPU clusters
- Handles requests in parallel
- Returns responses via cloud infrastructure (Azure, AWS, GCP)

---

## 🔄 In Simple Terms

| You Say…           | It Means…                                                |
|--------------------|----------------------------------------------------------|
| "I’m using GPT-4"  | You're sending input to a service running the GPT-4 model |
| "LLM answers me"   | The model is predicting and returning the next tokens     |
| "It's smart"       | It's trained to guess next words based on context         |
