from dotenv import load_dotenv
import os
import json
import re

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    api_key=groq_api_key
)

quiz_prompt = PromptTemplate.from_template("""
You are an AI quiz generator.

Generate {num_questions} multiple choice questions.

Topic: {topic}
Difficulty: {difficulty}

Return ONLY JSON.

Example format:

[
  {{
    "question": "What is Machine Learning?",
    "options": [
      "A method where computers learn from data",
      "A programming language",
      "A type of hardware",
      "A database system"
    ],
    "answer": "A method where computers learn from data"
  }}
]

Rules:
- options must be a list of exactly 4 items
- answer must be exactly one of the options
- return ONLY JSON
""")

def clean_json(text):
    """Extract JSON from LLM response"""
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return match.group()
    return text

def generate_quiz(topic, difficulty, num_questions):

    prompt = quiz_prompt.format(
        topic=topic,
        difficulty=difficulty,
        num_questions=num_questions
    )

    response = llm.invoke(prompt)

    cleaned = clean_json(response.content)

    try:
        quiz = json.loads(cleaned)
        return quiz
    except:
        return []