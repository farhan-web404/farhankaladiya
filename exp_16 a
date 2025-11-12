from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Text input field
        self.text_input = TextInput(hint_text="Enter something", multiline=False)
        layout.add_widget(self.text_input)

        # Button to display entered text
        button = Button(text="Show Text")
        button.bind(on_press=self.display_text)
        layout.add_widget(button)

        # Label to show output
        self.display_label = Label(text="")
        layout.add_widget(self.display_label)

        return layout

    def display_text(self, instance):
        entered_text = self.text_input.text
        self.display_label.text = entered_text

if __name__ == '__main__':
    TextInputApp().run()
