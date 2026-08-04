# 🤖 pyAI
> A lightweight, local AI assistant built in Python.

> pyAI is a fast terminal-based AI assistant that runs **completely locally**. It supports multiple 
  user profiles, persistent memory, chat history, image generation, browser integration, and much more.
  A stronger system (better CPU and GPU are perfect for faster responses), though it has been optimized
  to run even in normal or low-end systems.

## ✨ Features

- 💬 Local AI conversations
- 👤 Multiple user profiles
- 🔒 Password-protected profiles
- 🧠 Global long-term memory
- 📁 Automatic chat saving
- 🎨 AI image generation
- 🌐 Browser opening support
- ⚡ Streaming responses
- 📦 Modular Python architecture
- 💾 Persistent user data
- 🖥️ Terminal interface

## 📂 Project Structure

pyAI/
│
├── main.py
├── config.py
├── AI.py
├── memory.py
├── browser.py
├── images.py
├── profiles.py
├── chats.py
├── banner.py
├── dependencies.py
├── osinfo.py
├── LICENSE
├── README.md
│
│
├── Profiles/
│   ├── {username}/
│   ├── Chats/
│   ├── Images/
│   ├── memory.json
│   └── profile.json
├── platforms
│   ├── installer.py
│   ├── linux.py
│   ├── mac.py
│   ├── termux.py
│   └── windows.py

## 🚀 Installation

### 1. Clone the repository

bash
...
git clone https://github.com/Siddiqui-Brothers/pyAI.git
cd pyAI
```

### 2. Install Python

Python 3.11 or newer is recommended.
https://www.python.org/

### 3.🌍 Supported Platforms

- ✅ Windows
- ✅ Linux
- ✅ macOS
- ✅ Android (Termux)

### 4. Run pyAI
python main.py (in cmd after cd into pyAI folder)
On first launch, pyAI automatically:

- 📦 Installs its dependencies (it will ask (y/n)...
- ⚙️ Sets everything up automatically

Once setup is complete, pyAI is ready to use.

## 🧠 Memory System

pyAI remembers long-term information such as:

- Favourite colours
- Favourite games
- Favourite anime
- Devices
- Projects
- Goals
- Preferences
- Personal facts

Each profile has its own independent memory.

## 🎨 Image Generation

Simply ask something like:

```
Generate an image of a cyberpunk city at sunset.
```
or

```
Draw Makima in anime style.
```
pyAI automatically enhances your prompt before generating the image.

## 📜 License

This project is licensed under the **MIT License**.
See the LICENSE file for details.

## ❤️ Credits
Created with lots of Chai, debugging, and questionable life decisions by
*Siddiqui Brothers*:

- Muhammad Rayyan Siddiqui
- Muhammad Arshmaan Siddiqui

## ⭐ Future Plans

- Voice conversations
- Better memory engine
- Plugin system
- Tool calling
- File understanding
- Vision support
- Desktop GUI
- Better image generation
- Cross-platform installer

If you enjoy the project, consider leaving a ⭐ on GitHub!
Every star helps ❤️
Thank You for choosing pyAI ❤️