from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


# Builder.load_file("test1.kv")

class MyWidget(BoxLayout):
    pass

class Test1App(App):
    pass

if __name__=='__main__':

    Test1App().run()