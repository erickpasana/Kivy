from turtle import color
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
# kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __init__(self,):
        super(MyRoot, self).__init__()
    def Generate_number(self):
        self.random_label.text = str(random.randint(1, 1000))

class RandomNumberApp(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    app = RandomNumberApp()
    app.run()