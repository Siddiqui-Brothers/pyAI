import subprocess
import shutil

def install_package(package_name):

    subprocess.run([
        "brew",
        "install",
        package_name
    ])


def install_ollama_mac(model_name):

    print("macOS detected.")

    if shutil.which("brew") is None:

     print()

    print("Homebrew is required.")
    print("Please install Homebrew first.")
    print("https://brew.sh")

    return False

    choice = input("Install now? (Y/N) > ").lower()

    if choice != "y":
        return False

    install_package("ollama")

    subprocess.run([
        "ollama",
        "pull",
        model_name
    ])

    print("\nInstallation complete!")
    print("Restart pyAI.")

    return True