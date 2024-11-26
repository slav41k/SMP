class Calculator:
    def __init__(self):
        self.history = []
        self.memory = []
        self.decimal_places = 2

    def set_decimal_places(self):
        while True:
            try:
                self.decimal_places = int(input("Введіть кількість знаків після коми (1-10): "))
                if 1 <= self.decimal_places <= 10:
                    break
                else:
                    print("Будь ласка, введіть число від 1 до 10.")
            except ValueError:
                print("Введіть коректне число.")

    def calculate(self, num1, num2, operator):
        raise NotImplementedError("Метод calculate() не реалізовано в базовому класі.")

    def add_to_history(self, expression):
        self.history.append(expression)

    def show_history(self):
        if not self.history:
            print("Історія порожня.")
        else:
            print("Історія обчислень:")
            for entry in self.history:
                print(entry)


class BasicCalculator(Calculator):
    def calculate(self, num1, num2, operator):
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        else:
            raise ValueError("Невідомий оператор")
        
        self.add_to_history(f"{num1} {operator} {num2} = {result:.{self.decimal_places}f}")
        return result


class ScientificCalculator(BasicCalculator):
    def calculate(self, num1, num2, operator):
        if operator == '^':
            result = num1 ** num2
        elif operator == '√':
            result = num1 ** 0.5
        elif operator == '%':
            result = num1 % num2
        else:
            return super().calculate(num1, num2, operator)
        
        self.add_to_history(f"{num1} {operator} {num2} = {result:.{self.decimal_places}f}")
        return result