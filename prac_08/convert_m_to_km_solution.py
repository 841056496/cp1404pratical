"""
CP1404- GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
04/09/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    output_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def convert_miles_to_km(self):
        miles = self.validate_input()
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, change):
        miles = self.validate_input()
        new_miles = miles + change
        self.root.ids.input_miles.text = str(new_miles)
        self.convert_miles_to_km()

    def validate_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


if __name__ == "__main__":
    MilesToKmApp().run()
