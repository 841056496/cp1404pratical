from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handles greeting the user based on the entered name."""
        name = self.root.ids.input_name.text
        if name:
            self.root.ids.output_label.text = f"Hello {name}"
        else:
            self.root.ids.output_label.text = "Please enter your name"

    def handle_clear(self):
        """Handles clearing the input field and the label."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


if __name__ == "__main__":
    BoxLayoutDemo().run()
