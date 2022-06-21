
from kivymd.app import MDApp
from kivy.lang import Builder

# kv = """
# """
class Test2(MDApp):
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
        'language-vis': 'Visaya',
    }

    def action(self):
        label = self.root.ids.txt
        label.text = "This text is displayed after pressing button!"
        label.pos_hint= {'center_x': .8, 'center_y': 0.8}

    def build(self):
        return Builder.load_file("test2.kv")

if __name__=='__main__':
    Test2().run()
