from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load .env variables
load_dotenv()

# Get API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    api_key=groq_api_key
)

# Prompt template
tutor_prompt = PromptTemplate.from_template("""
You are an expert university tutor.

Explain the concept below in simple terms.

Structure your answer as:

1. Simple Explanation
2. Example
3. Real World Application
4. Summary

Topic: {topic}
""")

def explain_concept(topic):

    prompt = tutor_prompt.format(topic=topic)

    response = llm.invoke(prompt)

    return response.content