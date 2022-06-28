from tkinter import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse

from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.base import runTouchApp

Window.clearcolor = (0, .3, 0.2, 1.0)


class MainWidget(BoxLayout):
    # def __init__(self,**kwargs):
    #     super(MainWidget, self).__init__(**kwargs)
        # self.cols = 2

        # self.add_widget(Image(source = r"\cards\\1_club.png"))
        # self.greeting = TextInput(multiline=False)
        # self.add_widget(self.greeting)
    pass


class TestApp(App):
    # def build(self):
    #     Window.clearcolor = (1,1,1,1)
        # return MainWidget()
    pass

if __name__ == '__main__':
    app = TestApp()
    app.run()
