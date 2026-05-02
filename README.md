
# 🤖 Jarvis — Desktop Voice Assistant

> *"Sometimes you gotta run before you can walk."* — Tony Stark

A Python-based desktop voice assistant that listens to your voice commands and does the heavy lifting for you. Open websites, play music, search Wikipedia, get news, take notes — all hands-free.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Assistant](#running-the-assistant)
- [How to Use](#how-to-use)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Authors](#authors)

---

## 📖 About the Project

I built Jarvis as a mini project to explore how Python can be used to create a real-time voice-controlled desktop assistant. The idea was simple — instead of clicking around, just *talk* to your computer and it does the work.

The assistant uses your microphone to capture voice input, processes it using Google's Speech Recognition API, and then performs the requested action — whether that's opening YouTube, telling you the time, searching Wikipedia, or cracking a joke.

It's not perfect, but it works. And that's what matters.

---

## ✨ Features

Here's everything Jarvis can do right now:

| Category | What You Can Say | What Happens |
|---|---|---|
| 🌐 **Websites** | "Open YouTube" | Opens in your browser |
| 🌐 **Websites** | "Open Google" | Opens Google |
| 🌐 **Websites** | "Open GitHub" | Opens GitHub |
| 🌐 **Websites** | "Open Wikipedia" | Opens Wikipedia |
| 🌐 **Websites** | "Open Stack Overflow" | Opens Stack Overflow |
| 🔍 **Search** | "Search about Python" | Google search results |
| 🔍 **Search** | "How to make pizza" | Google search results |
| 📖 **Wikipedia** | "Tell me about Elon Musk" | Wikipedia summary |
| 📖 **Wikipedia** | "Who is APJ Abdul Kalam" | Wikipedia summary |
| 🎵 **Music** | "Play Believer" | Plays on YouTube |
| 🎵 **Music** | "Play Arijit Singh" | Plays on YouTube |
| 🗺️ **Maps** | "Where is Nagpur" | Opens Google Maps |
| 🕐 **Time** | "What is the time" | Tells current time |
| 📅 **Date** | "What is the date" | Tells today's date |
| 📰 **News** | "Latest news" | Top 5 headlines |
| 📝 **Notes** | "Write a note" | Saves your note |
| 📝 **Notes** | "Read note" | Reads saved notes |
| 💻 **Apps** | "Open VS Code" | Launches VS Code |
| 💻 **Apps** | "Open Excel" | Launches Excel |
| 💻 **Apps** | "Open PowerPoint" | Launches PowerPoint |
| 💻 **Apps** | "Open Word" | Launches Word |
| 💻 **Apps** | "Open Spotify" | Launches Spotify |
| 💻 **Apps** | "Open Telegram" | Launches Telegram |
| 😄 **Fun** | "Tell me a joke" | Tells a random joke |
| 💬 **Small Talk** | "How are you" | Friendly response |
| 💬 **Small Talk** | "Who are you" | Self introduction |
| 💬 **Small Talk** | "Are you single" | 😂 |
| ⚙️ **System** | "Switch window" | Alt + Tab |
| 🛑 **Stop** | "Stop" / "Exit" / "Bye" | Shuts down Jarvis |

---

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Speech Recognition:** Google Speech Recognition API (via `SpeechRecognition`)
- **Text to Speech:** `pyttsx3` (offline, no API needed)
- **Wikipedia Search:** `wikipedia` library
- **YouTube Playback:** `pywhatkit`
- **News Headlines:** NewsAPI (`requests`)
- **Jokes:** `pyjokes`
- **GUI Automation:** `pyautogui`
- **Platform:** Windows 10/11

---

## 🚀 Getting Started

Follow these steps and you'll have Jarvis running in under 5 minutes.

### Prerequisites

Make sure you have the following installed:

- ✅ **Python 3.12** — [Download here](https://www.python.org/downloads/release/python-3120/)
- ✅ **Working microphone** connected to your PC
- ✅ **Internet connection** (for speech recognition, Wikipedia, YouTube)

> ⚠️ **Important:** Use Python 3.12 only. Python 3.14 is not supported because `PyAudio` does not have a wheel for it yet.

---

### Installation

**Step 1 — Clone or download this project**

Place the file in your project folder. Example:
```
D:\Mini project code\desktop-voice-assistant.py
```

**Step 2 — Open terminal in that folder**

```bash
cd "D:\Mini project code"
```

**Step 3 — Install all required packages** (run this once)

```bash
"C:/Users/Mahesh Chaudhari/AppData/Local/Programs/Python/Python312/python.exe" -m pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pyjokes pyautogui requests pillow pyaudio
```

> If `pyaudio` fails, try:
> ```bash
> "C:/Users/Mahesh Chaudhari/AppData/Local/Programs/Python/Python312/python.exe" -m pip install pyaudio
> ```

---

### Running the Assistant

```bash
"C:/Users/Mahesh Chaudhari/AppData/Local/Programs/Python/Python312/python.exe" "d:/Mini project code/desktop-voice-assistant.py"
```

If everything is set up correctly, you will see:

```
==================================================
   JARVIS Voice Assistant — Ready!
==================================================

  🤖 Jarvis : Good Morning Sir!
  🤖 Jarvis : I am Jarvis. How can I help you?

  🎙️  Listening...
```

Now just speak into your microphone!

---

## 🗣️ How to Use

Once Jarvis is running, simply speak clearly into your microphone. Here are some example commands to try:

```
"Play Shape of You"         → plays on YouTube
"Tell me about India"       → Wikipedia summary
"What is the time"          → tells current time
"Where is Mumbai"           → opens Google Maps
"Open GitHub"               → opens github.com
"Tell me a joke"            → random joke
"Write a note"              → saves what you say
"Latest news"               → top 5 headlines (needs API key)
"Stop"                      → shuts down Jarvis
```

> 💡 Tip: Speak naturally at a normal pace. Jarvis listens for up to 8 seconds and pauses for 1 second before processing.

---

## ⚙️ Configuration

Open `desktop-voice-assistant.py` and fill in the CONFIG section at the top of the file:

```python
# ── Fill these paths for app launching to work ──
MUSIC_DIR       = r"C:\Users\Mahesh Chaudhari\Music"
VSCODE_PATH     = r"C:\Users\Mahesh Chaudhari\AppData\Local\Programs\Microsoft VS Code\Code.exe"
POWERPOINT_PATH = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
EXCEL_PATH      = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
WORD_PATH       = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
SPOTIFY_PATH    = r"C:\Users\Mahesh Chaudhari\AppData\Roaming\Spotify\Spotify.exe"
TELEGRAM_PATH   = r"C:\Users\Mahesh Chaudhari\AppData\Roaming\Telegram Desktop\Telegram.exe"

# ── For News feature ──
NEWS_API_KEY    = "your_api_key_here"
```

**Getting a free News API key:**
1. Go to [https://newsapi.org](https://newsapi.org)
2. Click "Get API Key" and sign up for free
3. Copy your key and paste it in `NEWS_API_KEY`

---

## 📁 Project Structure

```
D:\Mini project code\
│
├── desktop-voice-assistant.py    ← Main file (run this)
├── jarvis_notes.txt              ← Created automatically when you write a note
└── README.md                     ← You are reading this
```

---

## ⚠️ Known Issues

- **PyAudio on Python 3.14** — Not supported. Stick to Python 3.12.
- **Wikipedia DisambiguationError** — Some queries return multiple results. Try being more specific (e.g., "Tell me about Virat Kohli cricketer" instead of just "Virat Kohli").
- **Speech not recognized** — Can happen in noisy environments. Speak clearly and close to the mic.
- **pywhatkit YouTube delay** — `pywhatkit` opens a browser tab and waits a few seconds before playing. This is expected behavior.
- **News without API key** — The news feature won't work without a valid NewsAPI key. All other features work without it.

---

## 🔮 Future Improvements

Things I plan to add in the next version:

- [ ] Weather forecast by city name
- [ ] Send WhatsApp messages via pywhatkit
- [ ] Gmail integration (read/send emails)
- [ ] Reminder and alarm system
- [ ] Multi-language support (Hindi commands)
- [ ] Wake word detection ("Hey Jarvis")
- [ ] GUI dashboard with voice waveform

---

## 👨‍💻 Authors

**Mahesh & Team**
> Built as a Mini Project | Python | Voice AI | Desktop Automation



---

## 📄 License

This project is open source and free to use for educational purposes.

---
