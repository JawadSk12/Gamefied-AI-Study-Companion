from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.4,
    api_key=groq_api_key
)

study_plan_prompt = PromptTemplate.from_template("""
You are an expert study planner.

Create a {days}-day study plan for the subject: {subject}.

Rules:
- Each day should contain a clear topic.
- Topics should be ordered from beginner to advanced.
- Format exactly like this:

Day 1 - Topic
Day 2 - Topic
Day 3 - Topic

Return ONLY the study plan.
""")

def generate_study_plan(subject, days):

    prompt = study_plan_prompt.format(
        subject=subject,
        days=days
    )

    response = llm.invoke(prompt)

    return response.content