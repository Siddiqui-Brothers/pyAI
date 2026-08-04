import subprocess

def install_package(package_name):

    subprocess.run([
        "pkg",
        "install",
        "-y",
        package_name
    ])

def install_ollama_termux(model_name):

    print("Termux detected.")

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