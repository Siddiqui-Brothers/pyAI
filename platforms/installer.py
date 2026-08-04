from osinfo import *

from platforms.windows import install_ollama_windows
from platforms.linux import install_ollama_linux
from platforms.termux import install_ollama_termux
from platforms.mac import install_ollama_mac


def install_platform(model_name):

    if IS_WINDOWS:

        return install_ollama_windows(model_name)

    elif IS_TERMUX:

        return install_ollama_termux(model_name)

    elif IS_LINUX:

        return install_ollama_linux(model_name)

    elif IS_MAC:

        return install_ollama_mac(model_name)

    else:

        print("Unsupported Operating System.")

        return False
