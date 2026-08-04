import subprocess
from config import MODEL_NAME
from osinfo import *
from platforms.installer import install_platform


def check_dependencies():

    print("\nChecking pyAI dependencies...\n")
    print(f"Detected OS: {OS}")

    if IS_LINUX and not IS_TERMUX:
     print(f"Linux Distribution: {DISTRO}")

    if PACKAGE_MANAGER:
     print(f"Package Manager: {PACKAGE_MANAGER}")

    print()

    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True
        )

        if MODEL_NAME in result.stdout:
         print("✓ pyAI dependencies found.\n")
         return

    except Exception:
        pass

    print("pyAI dependencies are missing.\n")
    
    if install_platform(MODEL_NAME):

     print("✓ Dependencies installed.\n")

    else:

     print("Installation cancelled.")