from colorama import Fore, Style
from calc import BasicCalculator, ScientificCalculator

def main():
    print("Виберіть тип калькулятора:")
    print("1. Базовий калькулятор")
    print("2. Науковий калькулятор")

    while True:
        choice = input("Введіть номер типу калькулятора (1-2): ")
        if choice == '1':
            calculator = BasicCalculator()
            break
        elif choice == '2':
            calculator = ScientificCalculator()
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    color_map = {
        '1': Fore.WHITE,
        '2': Fore.RED,
        '3': Fore.GREEN,
        '4': Fore.YELLOW,
        '5': Fore.BLUE,
        '6': Fore.MAGENTA,
        '7': Fore.CYAN,
        '8': Fore.BLACK
    }

    print("1 WHITE")
    print("2 RED")
    print("3 GREEN")
    print("4 YELLOW")
    print("5 BLUE")
    print("6 MAGENTA")
    print("7 CYAN")
    print("8 BLACK")

    while True:
        choice = input("Введіть номер кольору (1-8): ")
        try:
            if choice in color_map:
                print(color_map[choice] + "Вибрано колір тексту" + Style.RESET_ALL)
                break
            else:
                raise ValueError("Невірний вибір. Введіть число від 1 до 8.")
        except ValueError as e:
            print(e)

    calculator.set_decimal_places()

    while True:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
        if operator != '√':
            num2 = float(input("Введіть друге число: "))
        else:
            num2 = None
        
        result = calculator.calculate(num1, num2, operator)
        print(f"Результат: {result:.{calculator.decimal_places}f}")

        again = input("Виконати ще одне обчислення? (y/n): ")
        if again.lower() != 'y':
            break

    calculator.show_history()
    print("Програма завершена.")


if __name__ == "__main__":
    main()