import os
import keyboard
from cube import Cube

class CubeRenderer:
    def __init__(self, size, color):
        self.cube = Cube(size, color)
        self.views = ["left corner", "front", "right corner", "front"]
        self.current_view_index = 0


    def render_view(self):
        if self.views[self.current_view_index] == "left corner":
            print(self.cube.draw_from_left_corner())
        elif self.views[self.current_view_index] == "front":
            print(self.cube.draw_side())
        elif self.views[self.current_view_index] == "right corner":
           print(self.cube.draw_from_right_corner())

    def next_view(self):
        self.current_view_index = (self.current_view_index + 1) % len(self.views)
        self.render_view()

    def previous_view(self):
        self.current_view_index = (self.current_view_index - 1) % len(self.views)
        self.render_view()

    def start_rendering(self):
        self.render_view()

        keyboard.on_press_key("right", lambda _: self.next_view())

        keyboard.on_press_key("left", lambda _: self.previous_view())

        keyboard.wait("esc")

