#Copyright (C) [2026] [Muhammad Rayyan Siddiqui and Muhammad Arshmaan Siddiqui]

#MIT LICENSE:
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files ("pyAI"), to deal
#in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
#sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#IN THE SOFTWARE.

#AGAIN, THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY OF LOSS, DAMAGE, OR ACCOUNTABILITY OF ANY KIND, USE THIS ON YOUR OWN RISK, THE CREATORS OF 
#"pyAI" WILL NOT BE CHARGED, COMPLAINED TO, OR WILL TAKE RESPONSIBILITY AS IT IS YOUR CHOICE TO INSTALL AND USE THIS SOFTWARE AS PROVIDED.

import os
import sys
import threading
import subprocess
import importlib
from osinfo import *

def ensure_python():

    try:

        subprocess.check_call([
            sys.executable,
            "--version"
        ], stdout=subprocess.DEVNULL,
           stderr=subprocess.DEVNULL)

    except Exception:

        print("Python is missing.")

        if IS_LINUX and not IS_TERMUX:

            print("Installing Python...")

            if PACKAGE_MANAGER == "apt":

                subprocess.check_call([
                    "sudo",
                    "apt",
                    "update"
                ])

                subprocess.check_call([
                    "sudo",
                    "apt",
                    "install",
                    "-y",
                    "python3"
                ])

            elif PACKAGE_MANAGER == "pacman":

                subprocess.check_call([
                    "sudo",
                    "pacman",
                    "-Sy",
                    "--noconfirm",
                    "python"
                ])

            elif PACKAGE_MANAGER == "dnf":

                subprocess.check_call([
                    "sudo",
                    "dnf",
                    "install",
                    "-y",
                    "python3"
                ])

            elif PACKAGE_MANAGER == "zypper":

                subprocess.check_call([
                    "sudo",
                    "zypper",
                    "install",
                    "-y",
                    "python3"
                ])

            elif PACKAGE_MANAGER == "apk":

                subprocess.check_call([
                    "sudo",
                    "apk",
                    "add",
                    "python3"
                ])

        else:

            print("Please install Python manually.")
            sys.exit(1)

def ensure_pip():

    try:

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "--version"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    except Exception:

        print("pip is missing.")

        if IS_LINUX and not IS_TERMUX:

         print("Installing pip...")

        if PACKAGE_MANAGER == "apt":

         subprocess.check_call([
            "sudo",
            "apt",
            "update"
        ])

         subprocess.check_call([
            "sudo",
            "apt",
            "install",
            "-y",
            "python3-pip"
        ])

        elif PACKAGE_MANAGER == "pacman":

         subprocess.check_call([
            "sudo",
            "pacman",
            "-Sy",
            "--noconfirm",
            "python-pip"
        ])

        elif PACKAGE_MANAGER == "dnf":

         subprocess.check_call([
            "sudo",
            "dnf",
            "install",
            "-y",
            "python3-pip"
        ])

        elif PACKAGE_MANAGER == "zypper":

         subprocess.check_call([
            "sudo",
            "zypper",
            "install",
            "-y",
            "python3-pip"
        ])

        elif PACKAGE_MANAGER == "apk":

         subprocess.check_call([
            "sudo",
            "apk",
            "add",
            "py3-pip"
        ])
    try:

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "--version"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        print("✓ pip installed.")

    except Exception:

        print("Failed to install pip.")
        sys.exit(1)

def install_package(import_name, pip_name):

    try:
        importlib.import_module(import_name)

    except ImportError:

        print(f"Installing {pip_name}...")

    try:

        command = [
            sys.executable,
            "-m",
            "pip",
            "install"
        ]

        if IS_LINUX and not IS_TERMUX:

            command.append("--break-system-packages")

        command.append(pip_name)

        subprocess.check_call(command)

    except subprocess.CalledProcessError:

       print(f"Failed to install {pip_name}.")
       sys.exit(1)
ensure_python()
ensure_pip()

install_package("ollama", "ollama")
install_package("requests", "requests")
install_package("distro", "distro")

from config import MAX_HISTORY, IMAGE_WORDS, EXIT_WORDS
from banner import startup_banner, history_banner, history_footer
from dependencies import check_dependencies
from profiles import choose_profile
from chats import choose_chat, save_chat
from memory import (
    load_memory,
    add_memory_to_prompt,
    update_memory
)
from AI import get_ai_response, generate_image_prompt
from images import generate_image
from browser import handle_browser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PROFILES_DIR = os.path.join(BASE_DIR, "Profiles")

if not os.path.exists(PROFILES_DIR):
    os.mkdir(PROFILES_DIR)

sys.stdout.reconfigure(encoding="utf-8")

startup_banner()
check_dependencies()

username, profile_path = choose_profile()

memory, memory_file = load_memory(profile_path)

print(f"Greetings, {username}! I am your personal AI Assistant. How can I assist you today?")

conversation, chat_path = choose_chat(username)

add_memory_to_prompt(
    conversation,
    username,
    memory
)

history_banner()

for message in conversation:

    if message["role"] == "system":
        continue

    elif message["role"] == "user":
        print(f"{username} > {message['content']}")

    elif message["role"] == "assistant":
        print(f"pyAI > {message['content']}")

history_footer()

while True:

    user_message = input(f"{username} > ")

    if user_message.lower() in [x.lower() for x in EXIT_WORDS]:
        print(f"pyAI > Goodbye {username}!")
        break

    words = user_message.lower().split()

    if any(word in words for word in IMAGE_WORDS):
       better_prompt = generate_image_prompt(user_message)
       generate_image(better_prompt, username)  
       continue

    conversation.append({
        "role": "user",
        "content": user_message
    })

    messages_to_send = [conversation[0]] + conversation[-MAX_HISTORY:]

    ai_reply = get_ai_response(messages_to_send)

    conversation.append({
        "role": "assistant",
        "content": ai_reply
    })

    save_chat(chat_path, conversation)

    threading.Thread(
     target=update_memory,
     args=(user_message, memory, memory_file),
     daemon=True
).start()

    handle_browser(ai_reply)