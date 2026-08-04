import webbrowser

def handle_browser(ai_reply):

    if ai_reply.startswith("OPEN_BROWSER:"):
        url = ai_reply.split("OPEN_BROWSER:")[1]

        print(f"pyAI > 🌐 Opening {url} in your default browser...")

        webbrowser.open(url)