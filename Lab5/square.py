from colorama import Fore

class Square:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        colors = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'cyan': Fore.CYAN,
            'white': Fore.WHITE,
            'black': Fore.BLACK
        }

        square_color = colors.get(self.color.lower(), Fore.WHITE)
        r = ""

        r += square_color + "+" + ("-" * int(self.size)) + "+\n"

        for _ in range(int(self.size / 3)):
            r += square_color + "|" + (" " * int(self.size)) + "|\n"

        r += square_color + "+" + ("-" * int(self.size)) + "+\n"

        return r
