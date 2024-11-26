import logging
import pandas as pd

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Calculator:
    """Базовий клас для калькулятора, що містить методи для обчислень."""
    
    def __init__(self):
        """Ініціалізація калькулятора з порожніми історією та пам'яттю."""
        self.history = []
        self.memory = []
        self.decimal_places = 2
        logging.info("Ініціалізація калькулятора.")

    def set_decimal_places(self):
        """Встановлює кількість знаків після коми для результатів обчислень."""
        while True:
            try:
                self.decimal_places = int(input("Введіть кількість знаків після коми (1-10): "))
                if 1 <= self.decimal_places <= 10:
                    logging.info("Кількість знаків після коми встановлено: %d", self.decimal_places)
                    break
            except ValueError:
                logging.error("Помилка введення: введіть коректне число.")
                print("Введіть коректне число.")

    def add_to_history(self, expression):
        """Додає вираз до історії обчислень."""
        self.history.append(expression)
        logging.info("Додано до історії: %s", expression)

    def show_history(self):
        """Відображає історію обчислень."""
        if not self.history:
            logging.info("Історія порожня.")
            print("Історія порожня.")
        else:
            logging.info("Відображення історії обчислень.")
            print("Історія обчислень:")
            for entry in self.history:
                print(entry)


class BasicCalculator(Calculator):
    """Клас для базових арифметичних обчислень."""
    
    def calculate(self, num1, num2, operator):
        """Виконує базові арифметичні операції: +, -, *, /."""
        logging.info("Обчислення: %d %s %d", num1, operator, num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                logging.error("Ділення на нуль неможливе.")
                raise ZeroDivisionError("Ділення на нуль неможливе.")
            result = num1 / num2
        else:
            logging.error("Невідомий оператор.")
            raise ValueError("Невідомий оператор")
        
        self.add_to_history(f"{num1} {operator} {num2} = {result:.{self.decimal_places}f}")
        return result


class ScientificCalculator(BasicCalculator):
    """Клас для наукових обчислень, що розширює BasicCalculator."""
    
    def calculate(self, num1, num2, operator):
        """Виконує наукові операції: ^, √, %."""
        logging.info("Наукове обчислення: %d %s %d", num1, operator, num2)
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


class DataLoader:
    """Клас для завантаження даних з CSV файлу."""
    
    def __init__(self, file_path):
        """Ініціалізація DataLoader з вказаним шляхом до файлу."""
        self.file_path = file_path
        self.data = None
        logging.info("Ініціалізація DataLoader з файлом: %s", file_path)

    def load_data(self):
        """Завантажує дані з CSV файлу."""
        try:
            self.data = pd.read_csv(self.file_path)
            logging.info("Дані успішно завантажено з %s", self.file_path)
        except pd.errors.EmptyDataError:
            logging.error("Файл порожній.")
            raise
        except pd.errors.ParserError:
            logging.error("Помилка парсингу даних.")
            raise
        except Exception as e:
            logging.error("Помилка при завантаженні даних: %s", e)
            raise

    def show_data(self):
        """Відображає завантажені дані."""
        if self.data is None or self.data.empty:
            logging.info("Дані не завантажені.")
            print("Дані не завантажені.")
        else:
            logging.info("Відображення завантажених даних.")
            print(self.data.head())


# Приклад використання класу
if __name__ == "__main__":
    FILE_PATH = "path/to/your/file.csv"
    loader = DataLoader(FILE_PATH)
    
    try:
        loader.load_data()
        loader.show_data()
    except Exception as e:
        logging.error("Сталася помилка: %s", e)