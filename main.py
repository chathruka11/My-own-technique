import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class PusaAI(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Display Area
        self.scroll = ScrollView()
        self.chat_history = Label(text="🐾 පූසා AI සූදානම්...\n", size_hint_y=None, halign='left', valign='top')
        self.chat_history.bind(size=self.update_scroll)
        self.scroll.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll)

        # Input Area
        self.input_layout = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.user_input = TextInput(multiline=False, hint_text="මොකක්ද මචං අද ප්ලෑන් එක?")
        self.send_btn = Button(text="Send", size_hint_x=None, width=80)
        self.send_btn.bind(on_press=self.send_message)
        
        self.input_layout.add_widget(self.user_input)
        self.input_layout.add_widget(self.send_btn)
        self.layout.add_widget(self.input_layout)
        
        return self.layout

    def update_scroll(self, *args):
        self.chat_history.text_size = (self.chat_history.width, None)
        self.chat_history.height = self.chat_history.texture_size[1]

    def send_message(self, instance):
        msg = self.user_input.text
        if msg:
            self.chat_history.text += f"\nඔයා: {msg}"
            response = self.get_ai_response(msg)
            self.chat_history.text += f"\nපූසා: {response}\n"
            self.user_input.text = ""

    def get_ai_response(self, text):
        return "මචං, මම දැන් APK එක ඇතුළේ වැඩ! අපි වීඩියෝ එක හදමුද?"

if __name__ == "__main__":
    PusaAI().run()
