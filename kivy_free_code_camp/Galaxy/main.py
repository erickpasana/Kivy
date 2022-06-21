from tkinter import VERTICAL
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    # line = None
    V_NB_LINES = 7
    VERTICAL_LINE_SPACING = 0.1     # percentage of screen width
    vertical_lines = [] 

    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"Init W:{str(self.width/2)} H:{str(self.height*0.75)}")
        self.init_vertical_lines()

    def on_parent(self, widget, parent):
        # print(f"On_Parent W:{str(self.width/2)} H:{str(self.height*0.75)}")
        pass

    def on_size(self, *args):
        # print(f"On_Size W: {self.width} H:{self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
        # pass

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass

    def init_vertical_lines(self,):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100,100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)
        spacing = self.VERTICAL_LINE_SPACING * self.width
        # self.line.points = [center_x, 0, center_x, 100]
        offset = -int(self.V_NB_LINES/2)
        # point_y = 0
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + offset*spacing)
            self.vertical_lines[i].points = [line_x, 0, line_x, self.height]
            offset += 1


class GalaxyApp(App):
    pass


if __name__ == '__main__':

    GalaxyApp().run()
