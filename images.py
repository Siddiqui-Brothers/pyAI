import os
import time
import requests
import urllib.parse
from AI import generate_image_prompt
from config import PROFILES_DIR

def generate_image(prompt, username):

    print("pyAI > Generating image...")

    prompt = urllib.parse.quote(prompt)
    better_prompt = generate_image_prompt(prompt)
    

    url = f"https://image.pollinations.ai/prompt/{better_prompt}?model=flux"

    image = requests.get(url)

    filename = os.path.join(
    PROFILES_DIR,
    username,
    "Images",
    f"{int(time.time())}.png"
)

    with open(filename, "wb") as f:
        f.write(image.content)

    print(f"pyAI > Image saved to {filename}")    