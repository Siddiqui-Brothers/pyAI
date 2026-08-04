import platform
import os
import distro


OS = platform.system()

IS_WINDOWS = OS == "Windows"
IS_LINUX = OS == "Linux"
IS_MAC = OS == "Darwin"

IS_TERMUX = (
    IS_LINUX and
    "com.termux" in os.environ.get("PREFIX", "")
)

DISTRO = distro.id().lower()

def get_package_manager():

    if IS_WINDOWS:
        return None

    if IS_TERMUX:
        return "pkg"

    if DISTRO in ["ubuntu", "debian", "linuxmint", "pop"]:
        return "apt"

    if DISTRO == "arch":
        return "pacman"

    if DISTRO == "fedora":
        return "dnf"

    if DISTRO == "opensuse":
        return "zypper"

    if DISTRO == "alpine":
        return "apk"

    return "unknown"

PACKAGE_MANAGER = get_package_manager()