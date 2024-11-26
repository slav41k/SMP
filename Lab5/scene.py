import keyboard
from colorama import Fore,Style
from cube import Cube
from cube_renderer import CubeRenderer


class Scene:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_scene(self):
        for shape in self.shapes:
            print(shape.draw())

    def render_one(self):
        print(self.shapes[len(self.shapes)-1].draw())

    # @staticmethod
    # def render_cube(size):
    #     renderer = CubeRenderer(size, )
    #     renderer.start_rendering()

    @staticmethod
    def display_menu():
        print(f"{Style.BRIGHT}{Fore.CYAN}Available Commands:")
        print(f"{Fore.GREEN}cube{Style.RESET_ALL} - Calculate the cube of a number")
        print(f"{Fore.GREEN}square{Style.RESET_ALL} - Calculate the square of a number")
        print(f"{Fore.GREEN}size{Style.RESET_ALL} - Display the size of the object")
        print(f"{Fore.GREEN}resize{Style.RESET_ALL} - Resize the object")
        print(f"{Fore.GREEN}color{Style.RESET_ALL} - Change the color of the object")
        print(f"{Fore.GREEN}render{Style.RESET_ALL} - Render the object")
        print(f"{Fore.GREEN}render_cube{Style.RESET_ALL} - Render the cube")
        print(f"{Fore.GREEN}save{Style.RESET_ALL} - Save the object")
        print(f"{Fore.RED}exit{Style.RESET_ALL} - Exit the program")
