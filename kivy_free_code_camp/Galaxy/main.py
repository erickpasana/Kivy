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
    V_NB_LINES = 8
    VERTICAL_LINE_SPACING = 0.2    # percentage of screen width
    vertical_lines = [] 

    H_NB_LINES = 6
    HORIZONTAL_LINE_SPACING = 0.15     # percentage of screen height
    horizontal_lines = [] 

    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"Init W:{str(self.width/2)} H:{str(self.height*0.75)}")
        self.init_vertical_lines()
        self.init_horizontal_lines()

    def on_parent(self, widget, parent):
        # print(f"On_Parent W:{str(self.width/2)} H:{str(self.height*0.75)}")
        pass

    def on_size(self, *args):
        # print(f"On_Size W: {self.width} H:{self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()
        self.update_horizontal_lines()

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
                self.horizontal_lines.append(Line())

    def update_vertical_lines(self):
        spacing = self.VERTICAL_LINE_SPACING * self.width
        central_line_x = int(self.width/2)      #  + spacing/2
        offset = -int(self.V_NB_LINES/2)+0.5
        for i in range(0, self.V_NB_LINES):
            line_x = int(central_line_x + offset*spacing)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def init_horizontal_lines(self,):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NB_LINES):
                self.horizontal_lines.append(Line())

    def update_horizontal_lines(self):
        central_line_x = int(self.width/2)      #  + spacing/2
        spacing = self.VERTICAL_LINE_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)+0.5

        xmin = central_line_x+offset*spacing
        xmax = central_line_x-offset*spacing
        for i in range(0, self.H_NB_LINES):
            line_y = i * self.HORIZONTAL_LINE_SPACING * self.height
            x1, y1 = self.transform(xmin,line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]
            offset += 1

    def transform(self,x,y):
        # return self.transform_2d(x,y)
        return self.transform_perpective(x,y)

    def transform_2d(self,x,y):
        return int(x),int(y)

    def transform_perpective(self,x,y):
        lin_y = y + self.perspective_point_y / self.height
        if lin_y > self.perspective_point_y:
            lin_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - lin_y
        factor_y = diff_y/self.perspective_point_y  # when 
        factor_y = pow(factor_y, 4)

        tr_x = self.perspective_point_x + diff_x * factor_y
        tr_y = (1 - factor_y) * self.perspective_point_y
        return int(tr_x),int(tr_y)



class GalaxyApp(App):
    pass


if __name__ == '__main__':

    GalaxyApp().run()
