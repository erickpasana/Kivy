from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from tkinter import VERTICAL
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.properties import Clock
from kivy.core.window import Window
from kivy import platform


class MainWidget(Widget):

    from transforms import transform, transform_2d, transform_perpective
    from user_actions import keyboard_closed, on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    # line = None
    V_NB_LINES = 10
    VERTICAL_LINE_SPACING = 0.25    # percentage of screen width
    vertical_lines = [] 

    H_NB_LINES = 5
    HORIZONTAL_LINE_SPACING = 0.15     # percentage of screen height
    horizontal_lines = [] 
    SPEED = 2
    current_offset_y = 0

    SPEED_X = 12
    current_speed_x = 0
    current_offset_x = 0

    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"Init W:{str(self.width/2)} H:{str(self.height*0.75)}")
        self.init_vertical_lines()
        self.init_horizontal_lines()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1/60)

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def init_vertical_lines(self,):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100, 0, 100,100])
            for i in range(0, self.V_NB_LINES):
                self.vertical_lines.append(Line())
                self.horizontal_lines.append(Line())

    def update_vertical_lines(self):
        central_line_x = int(self.width/2)      #  + spacing/2
        spacing = self.VERTICAL_LINE_SPACING * self.width
        offset = -int(self.V_NB_LINES/2)+0.5
        for i in range(0, self.V_NB_LINES):
            line_x = central_line_x + offset*spacing + self.current_offset_x
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

        xmin = central_line_x+offset*spacing + self.current_offset_x
        xmax = central_line_x-offset*spacing + self.current_offset_x
        spacing_y = self.HORIZONTAL_LINE_SPACING * self.height

        for i in range(0, self.H_NB_LINES):
            line_y = i * spacing_y - self.current_offset_y
            x1, y1 = self.transform(xmin,line_y)
            x2, y2 = self.transform(xmax, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]
            # offset += 1

    def update(self, dt):
        # print("update")
        self.update_vertical_lines()
        self.update_horizontal_lines()
        time_factor = dt*60
        self.current_offset_y += self.SPEED * time_factor

        spacing_y = self.HORIZONTAL_LINE_SPACING * self.height
        if self.current_offset_y >= spacing_y:
            self.current_offset_y -= spacing_y

        self.current_offset_x += self.current_speed_x * time_factor
        # self.current_speed_x = 0


class GalaxyApp(App):
    pass


if __name__ == '__main__':

    GalaxyApp().run()
