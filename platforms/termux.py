import subprocess
import shutil
import importlib
import sys


def install_package(package_name):

    print(f"Installing {package_name}...")

    subprocess.run([
        "pkg",
        "install",
        "-y",
        package_name
    ], check=True)


def install_python_package(package_name):

    try:

        importlib.import_module(package_name)
        print(f"✓ {package_name} already installed.")

    except ImportError:

        print(f"Installing {package_name}...")

        subprocess.run([
            sys.executable,
            "-m",
            "pip",
            "install",
            package_name
        ], check=True)


def ensure_termux_packages():

    print("Checking Termux packages...")

    packages = [
        "python",
        "curl",
        "git",
        "zstd"
    ]

    for package in packages:

        if shutil.which(package):

            print(f"✓ {package} already installed.")

        else:

            install_package(package)


    print("✓ Termux packages ready.")



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
    ], check=True)


    print("\nInstallation complete!")
    print("Restart pyAI.")

    return True