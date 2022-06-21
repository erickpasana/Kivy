
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class Test6(MDApp):

    def table(self):
        # screen = Screen()
        self.tables = MDDataTable(size_hint=(0.9, 0.6),
                                use_pagination=True,
                                column_data=[
                                    ("No.", dp(30)),
                                    ("Column 1", dp(30)),
                                    ("Column 2", dp(30)),
                                    ("Column 3", dp(30)),
                                    ("Column 4", dp(30)),
                                    ("Column 5", dp(30)),
                                ],
                                row_data=[
                                    (f"{i + 1}", "1", "2", "3", "4", "5") for i in range(50)
                                ],
                                )
        self.tables.open()
        # screen.add_widget(tables)
        # return screen

    def build(self):
        return Builder.load_file('test6.kv')


Test6().run()
