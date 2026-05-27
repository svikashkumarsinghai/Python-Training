Phase 1 — Python Basics (1–2 Weeks)
  Variables
  Data types
  Loops
  Functions
  Lists & Dictionaries
  File handling
  Exception handling
  OOP basics
Phase 2 — Python for Data Science (2 Weeks)
  NumPy
  Pandas
  Data cleaning
  Visualization
Phase 3 — Machine Learning Basics
  Regression
  Classification
  Train/test split
  Model evaluation
Phase 4 — Deep Learning
  Neural networks
  Tensors
  Training loops
  GPU basics
Phase 5 — Generative AI (Main Part)
  libraries:
  OpenAI:
    pip install openai
    Example:
      from openai import OpenAI
      client = OpenAI()      
      response = client.chat.completions.create(
          model="gpt-4.1-mini",
          messages=[{"role": "user", "content": "Hello"}]
      )      
      print(response.choices[0].message.content)
  LangChain:
    pip install langchain
    Prompt templates
    Chains
    Memory
    RAG
  Hugging Face
    pip install transformers
    Example:
      from transformers import pipeline
      generator = pipeline("text-generation")
      print(generator("AI will"))
Phase 6 — Build Real Projects
  Projects: 
  Chatbot
  PDF Q&A system
  AI Resume Analyzer
  AI Image Generator
  RAG application
  Voice assistant
    
  
