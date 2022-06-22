from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window


class MainWidget(Widget):
    pass


class TestApp(App):
    # def build(self):
    #     Window.clearcolor = (1,1,1,1)
    #     return MainWidget
    pass

if __name__ == '__main__':
    app = TestApp()
    app.run()