import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def call_llm(prompt: str):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


def research_agent(topic: str):
    prompt = f"""
    Research latest trends and insights about {topic}.
    Return bullet points with facts.
    """
    return call_llm(prompt)


def planner_agent(research_data: str):
    prompt = f"""
    Create a structured professional report outline from:
    {research_data}
    """
    return call_llm(prompt)


def writer_agent(outline: str):
    prompt = f"""
    Write a professional detailed report based on:
    {outline}
    """
    return call_llm(prompt)