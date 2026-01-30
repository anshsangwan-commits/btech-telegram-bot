import os
from dotenv import load_dotenv
from openai import OpenAI

# 🔑 Load .env file
load_dotenv()

# ✅ Create client with API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
