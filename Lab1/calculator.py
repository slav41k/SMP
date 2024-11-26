class Calculator:
    def __init__(self):
        self.num1 = 0.0
        self.num2 = 0.0
        self.operator = ""
    
    def get_input(self):
        try:
            self.num1 = float(input("Введіть перше число: "))
            self.operator = input("Введіть оператор (+, -, *, /, ^, √, %): ")
            self.num2 = float(input("Введіть друге число: ")) if self.operator != '√' else None
        except ValueError:
            print("Помилка: введіть правильне число.")
            self.get_input()  # Повторити введення, якщо була помилка

    def validate_operator(self):
        valid_operators = ['+', '-', '*', '/', '^', '√', '%']
        if self.operator not in valid_operators:
            print("Помилка: введено недійсний оператор.")
            return False
        return True

    def calculate(self):
        if not self.validate_operator():
            return
        
        try:
            if self.operator == '+':
                result = self.num1 + self.num2
            elif self.operator == '-':
                result = self.num1 - self.num2
            elif self.operator == '*':
                result = self.num1 * self.num2
            elif self.operator == '/':
                if self.num2 == 0:
                    raise ZeroDivisionError("Помилка: ділення на нуль.")
                result = self.num1 / self.num2
            elif self.operator == '^':
                result = self.num1 ** self.num2
            elif self.operator == '√':
                result = self.num1 ** 0.5
            elif self.operator == '%':
                result = self.num1 % self.num2
            
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Сталася помилка: {e}")

    def repeat_calculation(self):
        while True:
            self.get_input()
            self.calculate()
            again = input("Бажаєте виконати ще одне обчислення? (так/ні): ")
            if again.lower() != 'так':
                print("Дякуємо за використання калькулятора!")
                break

if __name__ == "__main__":
    calc = Calculator()
    calc.repeat_calculation()