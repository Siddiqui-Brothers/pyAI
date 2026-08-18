import ollama
import os
os.environ["OLLAMA_DEBUG"] = "0"
from config import MODEL_NAME

def get_ai_response(messages):

    stream = ollama.chat(
        model=MODEL_NAME,
        keep_alive="24h",
        stream=True,
        messages=messages
    )

    ai_reply = ""

    print("pyAI > ", end="", flush=True)

    for chunk in stream:
        piece = chunk["message"]["content"]
        ai_reply += piece
        print(piece, end="", flush=True)

    print()

    return ai_reply

def generate_image_prompt(user_prompt):

    IMAGE_PROMPT_SYSTEM = """
You are an expert AI image prompt engineer.

Convert user requests into professional image prompts.

Rules:
- Never explain anything.
- Never answer the user.
- Output ONLY the image prompt.
- Add quality tags.
- Add lighting.
- Add composition.
- Add art style.
- Add details.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": IMAGE_PROMPT_SYSTEM
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response["message"]["content"].strip()