import threading
from kivy.app import App
import ollama as o
from kivy.core.clipboard import Clipboard
import time
import random as r
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)
        self.last_space_time = 0
        self.skip_typing = False

    def copy(self):
        Clipboard.copy(self.full_text)
        self.ids.copy_b.text = "Copied!"
        Clock.schedule_once(self.reset_copy, 1)

    def reset_copy(self, dt):
        self.ids.copy_b.text = "Copy"

    def on_validate(self):
        self.ids.speech.text = "Loading..."
        self.load_list = ["-", "\\", "|", "/"]
        self.load_index = 0
        self.skip_typing = False

        self.loading_event = Clock.schedule_interval(self.animate_loading, 0.2)
        threading.Thread(target=self.get_response).start()

    def animate_loading(self, dt):
        if self.load_index == 4:
            self.load_index = 0
        self.ids.speech.text = "Loading..." + self.load_list[self.load_index]
        self.load_index += 1

    def get_response(self):
        text = self.ids.topic.text
        word_limit = int(self.ids.words.value)

        prompt = f"topic: {text}. Make me a paragraph on the given topic of about {word_limit+50} words"

        try:
            response = o.chat(
                model="llama2", messages=[{"role": "user", "content": prompt}]
            )
            content = response["message"]["content"]
        except Exception as e:
            content = f"Error from Ollama: {e}"

        Clock.schedule_once(lambda dt: self.start_typing(content), 0)
        threading.Thread(target=self.information).start()

    def start_typing(self, content):
        self.loading_event.cancel()
        self.full_text = content
        self.current_index = 0
        self.skip_typing = False
        Clock.schedule_interval(self.type_next_letter, 0.05)

    def type_next_letter(self, dt):
        if self.skip_typing:
            self.ids.speech.text = self.full_text
            self.ids.copy_b.disabled = False
            return False  # stop Clock

        if self.current_index <= len(self.full_text):
            if self.current_index >= 2:
                self.ids.speech.text = (
                    self.full_text[: (self.current_index - 2)]
                    + r.choice("abcdefghijklmnopqrstuvwxyz")
                    + r.choice("abcdefghijklmnopqrstuvwxyz")
                )
            else:
                self.ids.speech.text = self.full_text[: self.current_index]
            self.current_index += 1
        else:
            self.ids.information.text = "Enter your topic."
            self.ids.speech.text = self.full_text
            self.ids.copy_b.disabled = False
            return False

    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        if key == 32:  # Spacebar
            now = time.time()
            if now - self.last_space_time <= 0.4:
                print("Double space detected. Skipping typing.")
                self.skip_typing = True
            self.last_space_time = now

    def type_information(self, dt):
        if self.skip_typing:
            self.ids.information.text = "Enter your topic."
            return False
        if self.information_index < len(self.information_text):
            self.ids.information.text = self.information_text[: self.information_index]
            self.information_index += 1
        else:
            self.ids.information.text = self.information_text
            Clock.schedule_once(self.reset_information, 1)
            return False

    def information(self):
        self.information_text = "Press space bar twice to skip animation."
        self.information_index = 0
        Clock.schedule_interval(self.type_information, 0.1)

    def reset_information(self, dt):
        self.ids.information.text = "Enter your topic"


class SpeechApp(App):
    pass


SpeechApp().run()
