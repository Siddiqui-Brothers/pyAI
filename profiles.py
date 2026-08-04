import os
import json
import hashlib
from getpass import getpass
from banner import profile_banner
from config import PROFILES_DIR

def choose_profile():
    profile_banner()
    print("1. New Profile")
    print("2. Load Existing Profile")

    choice = input("\nChoice > ").strip()

    if choice == "1":
        username = input("Enter username > ").strip()
        password = getpass("Create password > ")
        confirm = getpass("Confirm password > ")   
        if password != confirm:
            print("Passwords do not match!")
            return choose_profile()
        password_hash = hashlib.sha256(
    password.encode()
).hexdigest()
        
        if not username:
            username = "User"

        profile_path = os.path.join(PROFILES_DIR, username)

        os.makedirs(os.path.join(profile_path, "Chats"), exist_ok=True)
        os.makedirs(os.path.join(profile_path, "Images"), exist_ok=True)
        memory_file = os.path.join(profile_path, "memory.json")

        if not os.path.exists(memory_file):
            with open(memory_file, "w") as f:
                json.dump({"facts": []}, f, indent=4)

        with open(os.path.join(profile_path, "profile.json"), "w") as f:
            json.dump({"username": username, "password": password_hash}, f, indent=4)

        print(f"\nCreated profile: {username}")
        return username, profile_path

    elif choice == "2":
        if not os.path.exists("Profiles"):
            print("No profiles found.")
            return choose_profile()

        profiles = [
    p for p in os.listdir(PROFILES_DIR)
    if os.path.isdir(os.path.join("Profiles", p))
]

        if not profiles:
            print("No profiles found.")
            return choose_profile()

        print()

        for i, profile in enumerate(profiles):
            print(f"{i+1}. {profile}")
        try:
            selected = int(input("\nProfile > "))

            if selected < 1 or selected > len(profiles):
                raise ValueError

        except ValueError:
            print("Invalid selection!")
            return choose_profile()

        username = profiles[selected - 1]

        profile_path = os.path.join(PROFILES_DIR, username)

        profile_file = os.path.join(profile_path, "profile.json")

        with open(profile_file, "r") as f:
            profile = json.load(f)
        entered_password = getpass("Password > ")
        entered_hash = hashlib.sha256(entered_password.encode()).hexdigest()
    
        if entered_hash != profile["password"]:
            print("\n❌ Incorrect password!")
            return choose_profile()

        print(f"\n✅ Welcome back, {username}!")
        return username, profile_path

    else:
        print("Invalid choice!")
        return choose_profile()