import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_topic(subject, topic):
    prompt = f"""
You are a B.Tech professor.
Explain the topic "{topic}" from subject "{subject}".

Rules:
- Exam oriented
- Simple language
- Bullet points
- 150–200 words
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
