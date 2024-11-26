import sys
from cube_renderer import CubeRenderer
from scene import Scene
from square import Square
from colorama import Fore,Style

class CommandLineInterface:
    def __init__(self):
        self.scene = Scene()

    def run(self):
        print("Welcome to the 3D ASCII Art Generator!")
        while True:
            Scene.display_menu()
            command = input(f"{Style.BRIGHT}{Fore.YELLOW}Enter a command: {Style.RESET_ALL}").lower()
            if command == "exit":
                sys.exit(0)
            elif command == "render":
                self.scene.render_scene()
            elif command == "cube":
                self.create_cube()
            elif command == "square":
                self.create_square()
                self.scene.render_one()
            elif command == "size":
                self.set_size()
                self.scene.render_one()
            elif command == "resize":
                self.resize_shape()
                self.scene.render_one()
            elif command == "color":
                self.set_color()
                self.scene.render_one()
            elif command == "save":
                self.save_to_file()
            else:
                print("Invalid command. Please try again.")

    def create_cube(self):
        size_input = input("Enter the size of the cube: ")
        try:
            size = float(size_input)
        except ValueError:
            print("Invalid input. Please enter a numeric size.")
            return
        color = input("Enter the color of the cube (e.g., red, green, blue, yellow, magenta, cyan, white, black ): ")
        cube = CubeRenderer(size, color)
        self.scene.add_shape(cube)
        print("Cube created.")
        print(cube.start_rendering())

    def create_square(self):
        size_input = input("Enter the size of the square: ")
        try:
            size = float(size_input)
        except ValueError:
            print("Invalid input. Please enter a numeric size.")
            return
        color = input("Enter the color of the square (e.g., red, green, blue, yellow, magenta, cyan, white, black ): ")
        square = Square(size, color)
        self.scene.add_shape(square)
        print("Square created.")

    def set_size(self):
        size = float(input("Enter the size for the current shape: "))
        if not self.scene.shapes:
            print("No shape to set size. Please create a shape first.")
            return
        current_shape = self.scene.shapes[-1]
        current_shape.size = size

    def resize_shape(self):
        scaling_factor = float(input("Enter the scaling factor for the current shape: "))
        if not self.scene.shapes:
            print("No shape to resize. Please create a shape first.")
            return
        current_shape = self.scene.shapes[-1]
        current_shape.size *= scaling_factor

    def set_color(self):
        if not self.scene.shapes:
            print("No shape to set color. Please create a shape first.")
            return
        color = input(
            "Enter the color for the current shape (e.g., red, green, blue, yellow, magenta, cyan, white, black): ")
        current_shape = self.scene.shapes[-1]
        current_shape.color = color
        print(f"Color set to {color} for the current shape.")

    def save_to_file(self):
        if not self.scene.shapes:
            print("No shapes to save. Please create a shape first.")
            return

        file_name = input("Enter the file name to save the ASCII art (include .txt extension): ")

        try:
            with open(file_name, "w") as file:
                for shape in self.scene.shapes:
                    ascii_art = shape.draw()
                    file.write(ascii_art + "\n\n")
            print(f"ASCII art saved to {file_name}.")
        except Exception as e:
            print(f"Error saving to file: {e}")


def main():
    cli = CommandLineInterface()
    cli.run()


if __name__ == "__main__":
    main()