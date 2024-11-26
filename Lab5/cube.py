from colorama import Fore

from colorama import Fore, Back, Style

class Cube:
    def __init__(self, size, color="white"):
        self.size = size
        self.color = color

    def draw_side(self):
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

        cube_color = colors.get(self.color.lower(), Fore.WHITE)

        size = int(self.size / 2)

        s, p, b, f, g, h, n = " ", cube_color + "+", cube_color + "|", cube_color + "\\", cube_color + "/", cube_color + "-", "\n"

        l = p + h * (size * 4) + p
        k = s * size
        r = ''

        t = v = 0

        half_size = int(size / 2)

        r +=  s * (half_size + 1) + p + h * (size * 3 - 1)  + p + n
        while t < half_size:
            t += 1
            r += s * (half_size - t + 1) + g + (size * 3 - half_size * (-t) - 1) * s + f + n

        r += l + n

        while v < self.size:
            v += 1
            r += b + s * size * 4 + b + n

        r += l + n

        return r

    def draw_from_left_corner(self):
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

            cube_color = colors.get(self.color.lower(), Fore.WHITE)

            size = int(self.size / 2)

            s, p, b, f, n = " ", cube_color + "+", cube_color + "|", cube_color + "\\", "\n"
            l = p + (cube_color + "-") * (size * 4) + p
            S = s * (4 * size)
            k = s * size
            r = l + n

            t = h = v = 0
            while t < size:
                r += b + (s * t) + f + (S + f + s * (size- size)) + n
                t += 1
            r += b + k + l + n

            while h <= size:
                r += b + k + b + S + b + n
                h += 1

            while v < size:
                v += 1
                r += (s * v) + f + (size - v) * s + b + S + b + n

            r += ((v + 1) * s) + l

            return r

    def draw_from_right_corner(self):
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

        cube_color = colors.get(self.color.lower(), Fore.WHITE)

        t = v = h = int(self.size / 2)
        s, p, b, f, n = " ", cube_color + "+", cube_color + "|", cube_color + "/", "\n"
        l = p + (cube_color + "-") * (t * 4) + p
        S = s * (4 * t)
        k = s * h
        K = b + S + b
        r = (s * t) + s + l + n
        while t:
            r += (s * t) + f + (S + f + s * (h - t) + b) + n
            t -= 1
        r += l + (k + b) + n + ((K + k + b + n) * (v - 1)) + K + k + p + n
        while v:
            v -= 1
            r += K + (s * v) + f + n
        r += l

        return r

