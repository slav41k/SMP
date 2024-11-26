# Функція для отримання коду кольору
def get_ansi_code(color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
    }
    return colors.get(color, '\033[0m')  # Повертає код кольору або за замовчуванням

# Глобальна змінна для збереження кольору
current_color = '\033[0m'

def set_text_color(color):
    global current_color
    current_color = get_ansi_code(color)

def get_text_color():
    return current_color

def change_text_color(self):
    available_colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
    print(f"Доступні кольори: {', '.join(available_colors)}")
    while True:
        color = input("Виберіть колір тексту: ").lower()
        if color in available_colors:
            set_text_color(color)  # Встановлюємо колір через app_settings
            print(f"{get_text_color()}Колір змінено на {color}\033[0m")  # Відображаємо повідомлення з вибраним кольором
            break
        else:
            print("Невірний колір. Спробуйте ще раз.")