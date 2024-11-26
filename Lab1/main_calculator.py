from calculator import Calculator
from app_settings import get_text_color

if __name__ == "__main__":
    calc = Calculator()
    calc.choose_text_color()  # Додано запит про колір тексту
    calc.choose_decimal_places()  # Додано запит про кількість знаків після коми
    text_color = get_text_color()  # Отримуємо вибраний колір

    print(f"{text_color}Ласкаво просимо до калькулятора!\033[0m")  # Виводимо повідомлення з вибраним кольором
    calc.get_input()
    result = calc.calculate()
    
    # Виводимо результат з вибраним кольором і кількістю знаків після коми
    calc.display_result(result)
    calc.save_to_memory(result)
    
    # Повторюємо обчислення
    calc.repeat()

    print(f"{text_color}Програма завершена\033[0m")