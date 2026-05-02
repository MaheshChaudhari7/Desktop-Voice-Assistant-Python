import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import time
import json
import requests
import pyjokes
import pywhatkit
import pyautogui

MUSIC_DIR       = r""
VSCODE_PATH     = r""
POWERPOINT_PATH = r""
EXCEL_PATH      = r""
WORD_PATH       = r""
SPOTIFY_PATH    = r""
TELEGRAM_PATH   = r""
NEWS_API_KEY    = ""

class Jarvis:

    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 170)
        self.engine.setProperty('volume', 1.0)
        print("=" * 50)
        print("   JARVIS Voice Assistant — Ready!")
        print("=" * 50)

    #speak
    def speak(self, text: str):
        print(f"\n  🤖 Jarvis : {text}")
        self.engine.say(text)
        self.engine.runAndWait()


    def greet(self):
        hour = datetime.datetime.now().hour
        if   0  <= hour < 12: self.speak("Good Morning Sir!")
        elif 12 <= hour < 18: self.speak("Good Afternoon Sir!")
        else:                 self.speak("Good Evening Sir!")
        self.speak("I am Jarvis. How can I help you?")

    #listen
    def listen(self) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\n  🎙️  Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            r.pause_threshold = 1.0
            try:
                audio = r.listen(source, timeout=8, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return ""
        try:
            print("  ⏳ Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"  🧑 You    : {query}")
            return query.lower()
        except sr.UnknownValueError:
            self.speak("Sorry Sir, I didn't catch that. Please repeat.")
        except sr.RequestError:
            self.speak("Speech service unavailable right now.")
        return ""

    #helpers
    def open_url(self, url: str, label: str = ""):
        if not url.startswith("http"):
            url = "https://" + url
        self.speak(f"Opening {label}, Sir.")
        webbrowser.open_new_tab(url)

    def open_app(self, path: str, name: str):
        if not path:
            self.speak(f"Path for {name} is not set in CONFIG section Sir.")
            return
        try:
            os.startfile(path)
            self.speak(f"Opening {name} Sir.")
        except Exception as e:
            self.speak(f"Could not open {name}.")
            print(f"  ❌ Error: {e}")

    #wikipedia
    def search_wikipedia(self, query: str):
        self.speak("Searching Wikipedia Sir...")
        for phrase in ["tell me about", "who is", "what is", "wikipedia", "search"]:
            query = query.replace(phrase, "").strip()
        try:
            result = wikipedia.summary(query, sentences=4, auto_suggest=False)
            self.speak("According to Wikipedia:")
            print(f"\n  📖 {result}\n")
            self.speak(result)
        except wikipedia.exceptions.DisambiguationError as e:
            self.speak(f"Multiple results found. Did you mean {e.options[0]}?")
        except wikipedia.exceptions.PageError:
            self.speak("Sorry Sir, no Wikipedia page found for that.")
        except Exception:
            self.speak("Something went wrong with Wikipedia search.")

    #news
    def get_news(self):
        if not NEWS_API_KEY:
            self.speak("News API key not set Sir. Please add it in the CONFIG section.")
            return
        try:
            url = f"https://newsapi.org/v2/top-headlines?country=in&pageSize=5&apiKey={NEWS_API_KEY}"
            res = requests.get(url, timeout=5).json()
            if res.get("status") != "ok":
                self.speak("Could not fetch news right now.")
                return
            self.speak("Here are today's top 5 headlines Sir:")
            print("\n  " + "=" * 45)
            for i, article in enumerate(res["articles"][:5], 1):
                title = article.get("title", "No title")
                print(f"  {i}. {title}")
                self.speak(f"{i}. {title}")
        except Exception as e:
            self.speak("Failed to get news.")
            print(f"  ❌ Error: {e}")

    #music
    def play_local_music(self):
        if not MUSIC_DIR:
            self.speak("Music directory not set in CONFIG Sir.")
            return
        try:
            songs = [f for f in os.listdir(MUSIC_DIR)
                    if f.lower().endswith(('.mp3', '.wav', '.flac', '.m4a'))]
            if not songs:
                self.speak("No music files found in music folder Sir.")
                return
            self.speak("Playing music Sir.")
            os.startfile(os.path.join(MUSIC_DIR, songs[0]))
        except Exception as e:
            self.speak("Could not play music.")
            print(f"  ❌ Error: {e}")

    #notes
    def write_note(self):
        self.speak("What should I write Sir?")
        note = self.listen()
        if not note:
            self.speak("Didn't hear anything. Note cancelled.")
            return
        self.speak("Should I include date and time?")
        ans = self.listen()
        with open("jarvis_notes.txt", "a", encoding="utf-8") as f:
            if "yes" in ans or "sure" in ans:
                ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{ts}] {note}\n")
            else:
                f.write(note + "\n")
        self.speak("Note saved Sir!")

    def read_note(self):
        try:
            with open("jarvis_notes.txt", "r", encoding="utf-8") as f:
                content = f.read().strip()
            if content:
                self.speak("Here are your notes Sir:")
                self.speak(content)
            else:
                self.speak("Notes file is empty Sir.")
        except FileNotFoundError:
            self.speak("No notes file found. Try writing a note first Sir.")

    #SWITCH WINDOW
    def switch_window(self):
        self.speak("Switching window Sir.")
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")


    def run(self):
        self.greet()

        while True:
            query = self.listen()
            if not query:
                continue

            #STOP
            if any(w in query for w in ["stop", "exit", "quit", "bye"]):
                self.speak("Goodbye Sir! Have a great day!")
                sys.exit(0)

            #WIKIPEDIA
            elif any(p in query for p in ["tell me about", "who is", "what is"]):
                self.search_wikipedia(query)

            #OPEN WEBSITES
            elif "open youtube" in query or "youtube" in query:
                self.open_url("youtube.com", "YouTube")

            elif "open google" in query or "google" in query:
                self.open_url("google.com", "Google")

            elif "open github" in query or "github" in query:
                self.open_url("github.com", "GitHub")

            elif "open wikipedia" in query or "wikipedia" in query:
                self.open_url("wikipedia.org", "Wikipedia")

            elif "open stack overflow" in query or "stack overflow" in query:
                self.open_url("stackoverflow.com", "Stack Overflow")

            #GOOGLE SEARCH
            elif any(p in query for p in ["search about", "search for", "how to make", "how to"]):
                search = query
                for p in ["search about", "search for", "how to make", "how to"]:
                    search = search.replace(p, "").strip()
                self.speak(f"Searching for {search} on Google.")
                self.open_url(f"https://www.google.com/search?q={search.replace(' ', '+')}", "Google Search")

            #YOUTUBE PLAY 
            elif "play" in query:
                song = query.replace("play", "").strip()
                if song:
                    self.speak(f"Playing {song} on YouTube.")
                    pywhatkit.playonyt(song)
                else:
                    self.play_local_music()

            #LOCAL MUSIC
            elif "music" in query:
                self.play_local_music()

            #DATE & TIME
            elif "time" in query:
                t = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"Sir, the time is {t}.")

            elif "date" in query:
                d = datetime.datetime.now().strftime("%d %B %Y")
                self.speak(f"Sir, today's date is {d}.")

            #NEWS
            elif any(p in query for p in ["news", "headlines", "latest news"]):
                self.get_news()

            #WHERE IS (MAPS)
            elif "where is" in query:
                place = query.replace("where is", "").strip()
                self.speak(f"Finding {place} on Google Maps.")
                self.open_url(
                    f"https://www.google.com/maps/place/{place.replace(' ', '+')}",
                    place
                )

            #OPEN APPS
            elif any(p in query for p in ["open vs code", "open code", "vs code"]):
                self.open_app(VSCODE_PATH, "VS Code")

            elif any(p in query for p in ["open powerpoint", "powerpoint"]):
                self.open_app(POWERPOINT_PATH, "PowerPoint")

            elif any(p in query for p in ["open excel", "excel"]):
                self.open_app(EXCEL_PATH, "Excel")

            elif any(p in query for p in ["open word", "ms word"]):
                self.open_app(WORD_PATH, "Word")

            elif any(p in query for p in ["open paint", "paint"]):
                self.open_app(PAINT_PATH, "Paint")

            elif any(p in query for p in ["open spotify", "spotify"]):
                self.open_app(SPOTIFY_PATH, "Spotify")

            elif any(p in query for p in ["open telegram", "telegram"]):
                self.open_app(TELEGRAM_PATH, "Telegram")

            #NOTES
            elif any(p in query for p in ["write a note", "take a note", "note likhna"]):
                self.write_note()

            elif any(p in query for p in ["read note", "tell me the note", "note padhna"]):
                self.read_note()

            #SWITCH WINDOW 
            elif "switch window" in query:
                self.switch_window()

            #JOKES
            elif "joke" in query:
                joke = pyjokes.get_joke()
                print(f"\n  😂 {joke}")
                self.speak(joke)

            #SMALL TALK
            elif "how are you" in query:
                self.speak("I am doing great Sir! How about you?")

            elif any(w in query for w in ["fine", "good", "great", "awesome"]):
                self.speak("Glad to hear that Sir! How can I assist you?")

            elif "what are you doing" in query:
                self.speak("Just waiting for your commands Sir.")

            elif "what is your use" in query or "what can you do" in query:
                self.speak(
                    "Sir I can open YouTube, Google, GitHub, Wikipedia, "
                    "play music, tell news, search Wikipedia, tell time and date, "
                    "open apps like VS Code Excel Word PowerPoint, "
                    "write and read notes, tell jokes and much more!"
                )

            elif "who are you" in query:
                self.speak(
                    "I am Jarvis, your personal desktop voice assistant Sir. "
                    "I am here to make your work easier."
                )

            elif "who made you" in query or "who created you" in query:
                self.speak("I was created by Yash and his team Sir.")

            elif "thank you" in query or "thanks" in query:
                self.speak("You are most welcome Sir!")

            elif "are you single" in query:
                self.speak("I am in a serious relationship with Wi-Fi Sir.")

            elif "jarvis" in query:
                self.speak("Yes Sir, how can I help you?")

            else:
                self.speak("Sorry Sir, I didn't understand that. Please try again.")

# START

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
