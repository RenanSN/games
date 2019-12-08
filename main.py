from kivy.uix.widget import Widget
from kivy.app import App
from kivy.config import Config

Config.read("config.ini")  # Chamando as configurações


class Pong(Widget):
    pass


class PongApp(App):
    def build(self):
        return Pong()


if __name__ == '__main__':
    PongApp().run()