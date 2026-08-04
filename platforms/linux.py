from osinfo import PACKAGE_MANAGER, DISTRO
import subprocess
import shutil
import time
import importlib
import sys

PACKAGE_NAMES = {

    "pip": {
        "apt": "python3-pip",
        "pacman": "python-pip",
        "dnf": "python3-pip",
        "yum": "python3-pip",
        "zypper": "python3-pip",
        "apk": "py3-pip",
        "xbps-install": "python3-pip",
        "default": "python3-pip"
    },

    "curl": {
        "default": "curl"
    },

    "zstd": {
        "default": "zstd"
    }

}

def command_exists(command):
    return shutil.which(command) is not None

def ensure_system_package(command_name, package_name):

    if command_exists(command_name):

        print(f"✓ {command_name} already installed.")
        return

    print(f"Installing {package_name}...")

    install_package(package_name)

def install_package(package_name):

        package_name = PACKAGE_NAMES.get(
            package_name,
            {"default": package_name}
        ).get(
            PACKAGE_MANAGER,
            PACKAGE_NAMES.get(
                package_name,
                {"default": package_name}
            )["default"]
        )

        print(f"Installing {package_name}...")

        if PACKAGE_MANAGER == "apt":

         command = [
            "sudo",
            "apt",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "pacman":

         command = [
            "sudo",
            "pacman",
            "-S",
            "--noconfirm",
            package_name
        ]

        elif PACKAGE_MANAGER == "dnf":

         command = [
            "sudo",
            "dnf",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "yum":

         command = [
            "sudo",
            "yum",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "zypper":

         command = [
            "sudo",
            "zypper",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "apk":

         command = [
            "sudo",
            "apk",
            "add",
            package_name
        ]

        elif PACKAGE_MANAGER == "xbps-install":

         command = [
            "sudo",
            "xbps-install",
            "-Sy",
            package_name
        ]

        elif PACKAGE_MANAGER == "emerge":

         command = [
            "sudo",
            "emerge",
            package_name
        ]

        elif PACKAGE_MANAGER == "eopkg":

         command = [
            "sudo",
            "eopkg",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "swupd":

         command = [
            "sudo",
            "swupd",
            "bundle-add",
            package_name
        ]

        elif PACKAGE_MANAGER == "nix":

         command = [
            "nix",
            "profile",
            "install",
            f"nixpkgs#{package_name}"
        ]

        elif PACKAGE_MANAGER == "pkg":

         command = [
            "sudo",
            "pkg",
            "install",
            "-y",
            package_name
        ]

        elif PACKAGE_MANAGER == "opkg":

         command = [
            "opkg",
            "install",
            package_name
        ]

        elif PACKAGE_MANAGER == "slackpkg":

         command = [
            "sudo",
            "slackpkg",
            "install",
            package_name
        ]

        elif PACKAGE_MANAGER == "tce-load":

         command = [
            "tce-load",
            "-wi",
            package_name
        ]

        elif PACKAGE_MANAGER == "petget":

         command = [
            "petget",
            package_name
        ]

        elif PACKAGE_MANAGER == "urpmi":

         command = [
            "sudo",
            "urpmi",
            package_name
        ]

        elif PACKAGE_MANAGER == "guix":

         command = [
            "guix",
            "install",
            package_name
        ]

        else:

         print(f"Unsupported package manager: {PACKAGE_MANAGER}")
         return False

        subprocess.run(command, check=True)
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

def ensure_linux_packages():
 
    
    print("Checking Linux packages...")

    ensure_system_package("python3", "python3")
    ensure_system_package("pip3", "pip")
    ensure_system_package("curl", "curl")
    ensure_system_package("zstd", "zstd")

    print("✓ Linux packages ready.")

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
