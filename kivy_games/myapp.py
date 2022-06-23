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


class MainWidget(GridLayout):
    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Hello"))
        self.greeting = TextInput(multiline=False)
        self.add_widget(self.greeting)


class TestApp(App):
    def build(self):
    #     Window.clearcolor = (1,1,1,1)
        return MainWidget()
    # pass

if __name__ == '__main__':
    app = TestApp()
    app.run()
