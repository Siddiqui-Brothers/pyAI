import os
import json
import ollama
import re
from config import MODEL_NAME

def load_memory(profile_path):

    memory_file = os.path.join(profile_path, "memory.json")

    if not os.path.exists(memory_file):
        with open(memory_file, "w") as f:
            json.dump({"facts": []}, f, indent=4)

    with open(memory_file, "r") as f:
        memory = json.load(f)

    return memory, memory_file

def add_memory_to_prompt(conversation, username, memory):

    conversation[0]["content"] += f"\nThe user's name is {username}."

    if memory["facts"]:

        conversation[0]["content"] += "\n\nThings you already know about this user:\n"

        for fact in memory["facts"]:
            conversation[0]["content"] += f"- {fact}\n"

def extract_memory(user_message):

    text = user_message.lower().strip()

    patterns = [

        (
            r"my favourite colour is (.+)",
            lambda m: f"The user's favourite colour is {m.group(1).strip()}."
        ),

        (
            r"my favorite color is (.+)",
            lambda m: f"The user's favourite colour is {m.group(1).strip()}."
        ),

        (
            r"i love (.+)",
            lambda m: f"The user likes {m.group(1).strip()}."
        ),

        (
            r"i own (.+)",
            lambda m: f"The user owns {m.group(1).strip()}."
        ),

        (
            r"my name is (.+)",
            lambda m: f"The user's name is {m.group(1).strip()}."
        ),
        (
            r"i am (.+)",
            lambda m: f"The user is {m.group(1).strip()}."
        ),

        (
            r"i'm (.+)",
            lambda m: f"The user is {m.group(1).strip()}."
        ),

        (
            r"i have (.+)",
            lambda m: f"The user has {m.group(1).strip()}."
        ),

        (
            r"i like (.+)",
            lambda m: f"The user likes {m.group(1).strip()}."
        ),

        (
            r"i dislike (.+)",
            lambda m: f"The user dislikes {m.group(1).strip()}."
        ),
    ]

    for pattern, builder in patterns:

        match = re.search(pattern, text)

        if match:
            return builder(match)

    return None

def update_memory(user_message, memory, memory_file):

    fact = extract_memory(user_message)

    if fact:

        if fact not in memory["facts"]:

          memory["facts"].append(fact)

          with open(memory_file, "w") as f:
            json.dump(memory, f, indent=4)

        return

    memory_prompt = f"""
The user said:

{user_message}

You are pyAI's memory manager.

You extract permanent user facts.

Only remember facts ABOUT THE USER.

Never remember facts about:
- history
- science
- mathematics
- programming
- books
- movies
- games
- famous people
- historical figures
- countries
- places
- random knowledge

If the fact is not describing the user, reply:

NO
Examples:
User: My favourite colour is blue.
YES: The user's favourite colour is blue.

User: I own a Pixel 7 Pro.
YES: The user owns a Pixel 7 Pro.

User: I'm building pyAI.
YES: The user is building pyAI.

User: Bahadur Shah I was a Mughal emperor.
NO

User: Python was created by Guido van Rossum.
NO

User: The capital of Japan is Tokyo.
NO

User: I think Tokyo is beautiful.
YES: The user likes Tokyo.

Read the user's message.

If it contains ANY long-term personal information, output exactly:

YES: <fact>

Examples:

User: My favourite colour is black.
YES: The user's favourite colour is black.

User: I own a Pixel 7 Pro.
YES: The user owns a Pixel 7 Pro.

User: I'm making an AI assistant.
YES: The user is building an AI assistant.

User: My name is Rayyan.
YES: The user's name is Rayyan.

If there is NO permanent information, output exactly:

NO

Do not explain.
Do not answer the user.
Only output YES: ... or NO.
"""

    memory_response = ollama.chat(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": memory_prompt
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
)
