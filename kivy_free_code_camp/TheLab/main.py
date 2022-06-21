#!/usr/bin/env python
from itertools import count
import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty, Clock, ObjectProperty
# from kivy.properties import ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color


class CanvasExample6(BoxLayout):
    pass


class CanvasExample5(Widget):
    pass


class CanvasExample4(Widget):
    # text = StringProperty("Still OK...")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos
        x += self.vx
        y += self.vy
        if y + self.ball_size > self.height:
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
            # self.vy = -self.vy
        self.ball.pos = (x, y)


class CanvasExample3(Widget):
    text = StringProperty("Still OK...")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            self.line = Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0, 1)
            self.cirlcle_Line = Line(circle=(400, 200,80), width=2)
            self.rect_line = Line(rectangle=(500, 350, 150, 100), width=2)
            self.rect = Rectangle(pos=(550, 150), size=(150, 100))
    def on_button_click(self):
        # print("foo")
        x, y = self.rect.pos
        w, h = self.rect.size
        incr = dp(10)
        diff = self.width - (x+w)
        #     self.rect.pos = (self.width, y)
        if diff < incr:
            incr = diff 
        if diff == 0:
            self.text = "That's enough!!!"

        x += incr
        self.rect.pos = (x, y)


class CanvasExample2(Widget):
    pass


class CanvasExample1(Widget):
    pass


class WidgetsExample(GridLayout):
    the_text = StringProperty("Hello!")
    count = 1
    button_state = BooleanProperty(False)
    txt_input_str = StringProperty("What's your name?")
    # slider_value_txt = StringProperty("Vol")

    def on_click(self):
        print("Button clicked")
        if self.button_state:
            self.the_text = f"{self.count}"
            self.count += 1
        else:
            pass

    def toggle_button_state(self, widget):
        print("Toggle button state: " + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.button_state = False
        else:
            widget.text = "ON"
            self.button_state = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
        # print(f"Slider value: {int(widget.value)}")  #+ str(int(widget.value)))
        # self.slider_value_txt = f"Vol {int(widget.value)}"
    
    # def vol_slider(self):
    #     self.slider_value = f"{self.slider_value}"
    def on_txt_validate(self, widget):
        self.txt_input_str = f"Hi {widget.text}. How are you?"
        widget.text = ""


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        size = dp(100)
        for i in range(1,101):
            b = Button (text=f"{i}", size_hint=(None,None), size=(size,size))
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass
    # def build(self):
    #     label = Label(text='Hello from Kivy',
    #                 size_hint=(.5, .5),
    #                 pos_hint={'center_x': .5, 'center_y': .5})

    #     return label

# if __name__ == '__main__':
# app = TheLabApp()
TheLabApp().run()