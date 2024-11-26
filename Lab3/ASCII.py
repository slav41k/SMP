import pyfiglet
from termcolor import colored
import os

class AsciiArtGenerator:  # Encapsulation
    def __init__(self):
        self.user_input = ""
        self.selected_font = "slant"
        self.selected_color = "white"
        self.ascii_art = ""

    def get_user_input(self):
        self.user_input = input("Введіть слово або фразу для генерації ASCII-арту: ").strip()
        while not self.user_input:
            self.user_input = input("Введення не може бути порожнім. Введіть слово або фразу: ").strip()

    def choose_font(self):
        supported_fonts = [
            "big", "block", "bulbhead", "chunky", "coinstak", "colossal", "computer",
            "doom", "epic", "isometric1", "isometric2", "isometric3", "isometric4",
            "larry3d", "nancyj-fancy", "rectangles", "roman", "rounded", "slant", "standard"
        ]

        print("Доступні шрифти (що підтримують українські символи):")
        for i, font in enumerate(supported_fonts):
            figlet = pyfiglet.Figlet(font=font)
            example_text = figlet.renderText("hello")
            print(f"{i + 1}. {font}\n{example_text}")

        while True:
            try:
                font_choice = int(input(f"Виберіть шрифт (1-{len(supported_fonts)}): ")) - 1
                if 0 <= font_choice < len(supported_fonts):
                    self.selected_font = supported_fonts[font_choice]
                    break
                else:
                    print("Невірний вибір. Виберіть номер зі списку.")
            except ValueError:
                print("Будь ласка, введіть коректне число.")

    def choose_color(self):
        colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        print("Доступні кольори: ", ", ".join(colors))

        self.selected_color = input("Виберіть колір для вашого ASCII-арту: ").lower().strip()
        while self.selected_color not in colors:
            self.selected_color = input("Невірний колір. Будь ласка, виберіть один із запропонованих кольорів: ").lower().strip()

    def generate_art(self):
        try:
            figlet = pyfiglet.Figlet(font=self.selected_font)
            self.ascii_art = figlet.renderText(self.user_input)
        except pyfiglet.FontNotFound:
            print("Шрифт не знайдено. Використовується стандартний шрифт.")
            self.selected_font = "slant"
            figlet = pyfiglet.Figlet(font=self.selected_font)
            self.ascii_art = figlet.renderText(self.user_input)

    def preview_art(self):
        print("\nПопередній перегляд:")
        print(colored(self.ascii_art, self.selected_color))

    def save_to_file(self):
        while True:
            try:
                file_name = input("Введіть назву файлу для збереження (без розширення): ").strip() + ".txt"
                if not file_name:
                    print("Назва файлу не може бути порожньою.")
                elif os.path.exists(file_name):
                    overwrite = input(f"Файл {file_name} вже існує. Перезаписати його? (y/n): ").lower().strip()
                    if overwrite == 'y':
                        break
                    else:
                        continue
                else:
                    break
            except Exception as e:
                print(f"Сталася помилка: {e}")

        try:
            with open(file_name, "w", encoding='utf-8') as file:
                file.write(self.ascii_art)
            print(f"ASCII-арт збережено у файл {file_name}")
        except IOError as e:
            print(f"Помилка при збереженні файлу: {e}")

class ResizableAsciiArtGenerator(AsciiArtGenerator):
    def resize_art(self, width, height):
        resized_art = self.ascii_art.split('\n')
        resized_art = [line[:width] for line in resized_art][:height]
        self.ascii_art = '\n'.join(resized_art)

    def changeSymbol(self, art, symbol):
        for char in art:
            if char != '\n' and char != ' ':
                art = art.replace(char, symbol)
        return art

    def use_custom_symbol(self):
        use_custom_char = input("Чи хочете ви використовувати власні символи замість стандартних? (y/n): ").lower().strip()
        if use_custom_char == 'y':
            while True:
                try:
                    symbol = input("Введіть символ для створення ASCII-арту (наприклад, @, #, *): ").strip()
                    if len(symbol) == 1 and ord(symbol) < 128:
                        self.ascii_art = self.changeSymbol(self.ascii_art, symbol)
                        break
                    else:
                        print("Будь ласка, введіть лише один ASCII-символ (без спеціальних символів, як ♥).")
                except ValueError:
                    print("Введення некоректне. Спробуйте ще раз.")

class AsciiArtApplication:
    def __init__(self, generator_class):
        self.generator = generator_class()

    def run(self):
        while True:
            self.generator.get_user_input()
            self.generator.choose_font()
            self.generator.choose_color()
            self.generator.generate_art()

            resize = input("Чи бажаєте ви змінити розмір ASCII-арту? (y/n): ").lower().strip()
            if resize == 'y':
                while True:
                    try:
                        width = int(input("Введіть ширину ASCII-арту (наприклад, 80): "))
                        height = int(input("Введіть висоту ASCII-арту (наприклад, 20): "))
                        self.generator.resize_art(width, height)
                        break
                    except ValueError:
                        print("Будь ласка, введіть числові значення для ширини та висоти.")

            use_custom = input("Чи хочете ви використовувати власні символи? (y/n): ").lower().strip()
            if use_custom == 'y':
                self.generator.use_custom_symbol()

            self.generator.preview_art()

            save = input("Чи бажаєте ви зберегти цей ASCII-арт у файл? (y/n): ").lower().strip()
            if save == 'y':
                self.generator.save_to_file()

            another = input("Чи хочете ви згенерувати ще один ASCII-арт? (y/n): ").lower().strip()
            if another != 'y':
                print("Дякуємо за використання ASCII-арт генератора!")
                break

if __name__ == "__main__":
    app = AsciiArtApplication(ResizableAsciiArtGenerator)
    app.run()