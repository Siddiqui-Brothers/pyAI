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

DISTRO = distro.name(pretty=True)

def get_package_manager():

    if IS_WINDOWS:
        return None

    if IS_TERMUX:
        return "pkg"

    if os.path.exists("/usr/bin/apt"):
        return "apt"

    if os.path.exists("/usr/bin/pacman"):
        return "pacman"

    if os.path.exists("/usr/bin/dnf"):
        return "dnf"

    if os.path.exists("/usr/bin/yum"):
        return "yum"

    if os.path.exists("/usr/bin/zypper"):
        return "zypper"

    if os.path.exists("/sbin/apk") or os.path.exists("/usr/bin/apk"):
        return "apk"

    if os.path.exists("/usr/bin/xbps-install"):
        return "xbps-install"

    if os.path.exists("/usr/bin/emerge"):
        return "emerge"

    if os.path.exists("/usr/bin/eopkg"):
        return "eopkg"

    if os.path.exists("/usr/bin/swupd"):
        return "swupd"

    if os.path.exists("/usr/bin/nix"):
        return "nix"

    if os.path.exists("/usr/sbin/pkg") or os.path.exists("/usr/bin/pkg"):
        return "pkg"

    if os.path.exists("/usr/bin/opkg"):
        return "opkg"

    if os.path.exists("/usr/sbin/slackpkg"):
        return "slackpkg"

    if os.path.exists("/usr/bin/tce-load"):
        return "tce-load"

    if os.path.exists("/usr/sbin/petget"):
        return "petget"

    if os.path.exists("/usr/sbin/urpmi"):
        return "urpmi"

    if os.path.exists("/usr/bin/guix"):
        return "guix"

    return "unknown"

PACKAGE_MANAGER = get_package_manager()