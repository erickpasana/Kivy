from kivymd.app import MDApp
from kivy.lang import Builder

class MyToDo(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
        
        return Builder.load_string('mytodo.kv')
        
    def add_task_high(self):
        print("Save the task as severity 1 in the DB and show in list")

    def call(self, obj):
        if obj.icon == "priority-high":
            self.add_task_high()
        elif obj.icon == "priority-low":
            print("Save the task as severity 2 in the DB")
        else:
            print("Mark the task as done in the DB")
if __name__ == "__main__":
    MyToDo().run()