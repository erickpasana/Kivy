from kivymd.app import MDApp
from kivy.lang import Builder


class Test5App(MDApp):

    def build(self):
        return Builder.load_file('test5.kv')


if __name__ == "__main__":

    Test5App().run()