from osinfo import PACKAGE_MANAGER, DISTRO
import subprocess
import shutil
import time
import importlib
import sys

def command_exists(command):
    return shutil.which(command) is not None

def ensure_system_package(command_name, package_name):

    if command_exists(command_name):

        print(f"✓ {command_name} already installed.")
        return

    print(f"Installing {package_name}...")

    install_package(package_name)

def install_package(package_name):
    print(f"Installing {package_name}...")

    if PACKAGE_MANAGER == "apt":

     subprocess.run([
    "sudo",
    "apt",
    "install",
    "-y",
    package_name
], check=True)

    elif PACKAGE_MANAGER == "pacman":

      subprocess.run([
    "sudo",
    "pacman",
    "-S",
    "--noconfirm",
    package_name
], check=True)

    elif PACKAGE_MANAGER == "dnf":

      subprocess.run([
    "sudo",
    "dnf",
    "install",
    "-y",
    package_name
], check=True)

    elif PACKAGE_MANAGER == "zypper":

      subprocess.run([
    "sudo",
    "zypper",
    "install",
    "-y",
    package_name
], check=True)

    elif PACKAGE_MANAGER == "apk":

      subprocess.run([
    "sudo",
    "apk",
    "add",
    package_name
], check=True)

    else:

      print("Unknown package manager")
      return False
    return True

def install_python_package(package_name):

    command = [
        sys.executable,
        "-m",
        "pip",
        "install"
    ]

    if DISTRO in ["ubuntu", "debian"]:
        command.append("--break-system-packages")

    command.append(package_name)

    subprocess.run(command, check=True)

def ensure_python_package(import_name, package_name):

    try:

        importlib.import_module(import_name)

        print(f"✓ {package_name} already installed.")

    except ImportError:

        print(f"Installing {package_name}...")

        install_python_package(package_name)

def install_ollama_linux(model_name):
    print("Linux detected.")
    choice = input("Install now? (Y/N) > ").lower()
    if choice != "y":
        return False

    ensure_system_package("curl", "curl")
    ensure_system_package("zstd", "zstd")

    ensure_python_package("ollama", "ollama")
    ensure_python_package("requests", "requests")
    ensure_python_package("PIL", "Pillow")
    ensure_python_package("distro", "distro")
    
    if not command_exists("ollama"):

        print("Installing Ollama...")

        subprocess.run([
            "sh",
            "-c",
            "curl -fsSL https://ollama.com/install.sh | sh"
        ], check=True)

    else:

        print("✓ Ollama already installed.")
    
    try:

        subprocess.run(
            ["ollama", "list"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
 
        print("✓ Ollama service already running.")

    except subprocess.CalledProcessError:

        print("Starting Ollama service...")

    subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    import time
    time.sleep(3)

    subprocess.run([
    "ollama",
    "pull",
    model_name
], check=True)
    
    print("\nInstallation complete!")
    print("Launching pyAI...")


    return True
