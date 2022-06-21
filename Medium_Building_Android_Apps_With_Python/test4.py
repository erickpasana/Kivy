from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class Test4(MDApp):
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_file('test4.kv')

    def auth(self):
        if self.root.in_class.text == 'root':
            # label = self.root.ids.show
            # label.text = "Sucess"
            self.dialog = MDDialog(title='Password check',
                    text="Sucess !", size_hint=(0.8, 1),
                    buttons=[MDFlatButton(text='Close', on_release=self.close_dialog),
                            MDFlatButton(text='More')]
                    )
            self.dialog.open()
        else:
            # label = self.root.ids.show
            # label.text = "Fail"
            self.dialog.text = 'Fail !'
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


Test4().run()