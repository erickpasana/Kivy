from kivymd.app import MDApp
from kivy.lang import Builder
# from kivymd.mdbutton import MDButton


class Test1(MDApp):
    def build(self):
        return Builder.load_file("test1.kv")


if __name__=='__main__':
    Test1().run()