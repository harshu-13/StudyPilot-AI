from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "llama-3.1-8b-instant"


def generate_answer(context, question):
    prompt = f"""
You are an AI Study Buddy.

Answer ONLY using the context below.

If the answer is not present in the context, reply exactly:
"I couldn't find that information in the uploaded notes."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def generate_summary(context):
    prompt = f"""
You are an AI Study Buddy.

Read the notes below and create a concise summary.

Requirements:
- Maximum 200 words
- Use bullet points
- Highlight important concepts
- Make it easy for students to revise.

Notes:
{context}

Summary:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content


def generate_quiz(context):
    prompt = f"""
You are an AI Study Buddy.

Generate 5 multiple-choice questions based ONLY on the notes below.

Rules:
- Each question should have 4 options (A, B, C, D).
- Clearly indicate the correct answer after each question.
- Do not use information outside the notes.

Notes:
{context}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content