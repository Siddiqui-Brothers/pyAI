import shutil
import subprocess


def has_winget():
    return shutil.which("winget") is not None

def install_ollama_windows(model_name):

    print("Windows detected.")

    if not has_winget():
        print("Automatic installation isn't available.")
        return False
    choice = input("Install now? (Y/N) > ").lower()

    if choice != "y":
        return False
    subprocess.run([
        "winget",
        "install",
        "-e",
        "--id",
        "Ollama.Ollama",
        "--accept-package-agreements",
        "--accept-source-agreements"
    ])

    subprocess.run([
        "ollama",
        "pull",
        model_name
    ])

    print("\nInstallation complete!")
    print("Restart pyAI.")

    return True