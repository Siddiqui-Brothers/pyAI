import os
import json

from config import SYSTEM_PROMPT
from banner import chat_banner, history_banner, history_footer
from config import PROFILES_DIR

def choose_chat(username):
    chat_banner()
    print("1. New Chat")
    print("2. Open Existing Chat")

    choice = input("\nChoice > ")

    if choice == "1":
        chat_name = input("Enter chat name > ")

        if not chat_name.strip():
            chat_name = "Untitled"

        chat_path = os.path.join(
    PROFILES_DIR,
    username,
    "Chats",
    f"{chat_name}.json"
)

        conversation = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]   

        with open(chat_path, "w") as f:
            json.dump(conversation, f, indent=4)

        print(f"\nCreated chat: {chat_name}")
        return conversation, chat_path

    elif choice == "2":
        chats_folder = os.path.join(
            PROFILES_DIR,
            username,
            "Chats"
        )

        chats = [
            f for f in os.listdir(chats_folder)
            if f.endswith(".json")
        ]

        if not chats:
            print("No saved chats found!")
            return choose_chat(username)

        print("\nAvailable Chats:")

        for i, chat in enumerate(chats, start=1):
            print(f"{i}. {chat[:-5]}")

        selected = int(input("\nOpen chat > "))

        chat_path = os.path.join(
    chats_folder,
    chats[selected - 1]
)

        with open(chat_path, "r") as f:
            conversation = json.load(f)

        print(f"\nLoaded {chats[selected - 1][:-5]}")
        return conversation, chat_path

    else:
        print("Invalid choice!")
        return choose_chat(username)

def save_chat(chat_path, conversation):
    with open(chat_path, "w") as f:
        json.dump(conversation, f, indent=4)