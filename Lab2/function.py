import math
from constants import global_var_calculator

history = []

def get_number(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 'm':
            memory_value = recall_memory()
            if memory_value is not None:
                return memory_value
            else:
                print("Пам'ять порожня, введіть інше число")
        else:
            try:
                return float(user_input)
            except ValueError:
                print("Введено недійсне число. Спробуйте ще раз")

def get_operator():
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^, %, √): ")
        if operator in ['+', '-', '*', '/', '^', '%', '√']:
            return operator
        print("Невірний оператор. Спробуйте ще раз")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return num1 / num2
    elif operator == '^':
        return num1 ** num2
    elif operator == '√':
        return num1 ** 0.5
    elif operator == '%':
        return num1 % num2
    else:
        raise ValueError("Невідомий оператор")

def save_to_memory(result):
    global_var_calculator.memory.append(result)
    print(f"Результат {result} збережено в пам'ять")

def recall_memory():
    if not global_var_calculator.memory:
        print("Пам'ять порожня")
        return None
    print("Доступні значення в пам'яті:")
    for i, value in enumerate(global_var_calculator.memory):
        print(f"{i + 1}: {value}")
    while True:
        try:
            index = int(input("Введіть номер значення, яке хочете використати: ")) - 1
            if 0 <= index < len(global_var_calculator.memory):
                return global_var_calculator.memory[index]
            else:
                print("Невірний номер. Спробуйте ще раз")
        except ValueError:
            print("Введіть коректний номер")

def show_history():
    if not history:
        print("Історія порожня")
    else:
        print("Історія обчислень")
        for entry in history:
            print(entry)

def add_to_history(num1, num2, operator, result):
    if num2 is not None:
        history.append(f"{num1} {operator} {num2} = {result}")
    else:
        history.append(f"{operator}{num1} = {result}")

def clear_memory():
    global_var_calculator.memory.clear()
    print("Пам'ять очищена")