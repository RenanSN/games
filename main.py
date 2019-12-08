from kivy.uix.widget import Widget
from kivy.app import App


class Pong(Widget):
    pass


class PongApp(App):
    def build(self):
        return Pong()


if __name__ == '__main__':
    PongApp().run()