import math

class NegativeExponentError(Exception):
    def __init__(self, message = "Зведення в негативний ступінь не дозволено"):
        self.message = message
        super().__init__(self.message)

class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            print(f'Помилка додавання: {e}')

    def subtract(self, a, b):
        try:
            return a - b
        except Exception as e:
            print(f'Помилка віднімання: {e}')

    def multiply(self, a, b):
        try:
            return a * b
        except Exception as e:
            print(f'Помилка множення: {e}')

    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе")
            return a / b
        except ZeroDivisionError as e:
            print(f"Помилка ділення: {e}")
        except Exception as e:
            print(f"Інша помилка ділення: {e}")

    def power(self, a, b):
        try:
            if b < 0:
                raise NegativeExponentError
            return a ** b
        except NegativeExponentError as e:
            print(f"Помилка зведення в ступінь: {e}")
        except Exception as e:
            print(f"Інша помилка зведення в ступінь: {e}")

    def sqrt(self, a):
        try:
            if a < 0:
                raise ValueError("Квадратний корінь з від'ємного числа не визначений")
            return math.sqrt(a)
        except ValueError as e:
            print(f"Помилка вилучення квадратного кореня: {e}")
        except Exception as e:
            print(f"Інша помилка вилучення квадратного кореня: {e}")


def get_numbers():
        while True:
            try:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))
                return a, b
            except ValueError:
                print("Помилка: введіть коректне число.")

calc = Calculator()

while True:
    print("\nОберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Зведення в ступінь")
    print("6. Вилучення квадратного кореня")
    print("7. Вихід")

    choice = input("Ваш вибір: ")

    if choice == '7':
        print("Дякуємо за використання калькулятора!")
        break

    if choice in ['1', '2', '3', '4', '5']:
        a, b = get_numbers()

    if choice == '1':
        result = calc.add(a, b)
    elif choice == '2':
        result = calc.subtract(a, b)
    elif choice == '3':
        result = calc.multiply(a, b)
    elif choice == '4':
        result = calc.divide(a, b)
    elif choice == '5':
        result = calc.power(a, b)
    elif choice == '6':
        while True:
            try:
                a = float(input("Введіть число для вилучення квадратного кореня: "))
                result = calc.sqrt(a)
                break
            except ValueError:
                print("Помилка: введіть коректне число.")
    else:
        print("Невірний вибір, спробуйте ще раз.")
        continue

    if result is not None:
        print(f"Результат: {result}")

    exit_choice = input("Бажаєте завершити програму? (y/n): ").lower()
    if exit_choice == 'y':
        print("Дякуємо за використання калькулятора!")
        break
