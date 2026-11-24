print("=== Калькулятор в Python===")
def main():
    num1 = float(input("Введите первое число:  "))
    num2 = float(input("Введите второе число:  "))
    operation = input("Выберите операцию (+, -, *, /): ")

    try:
        if operation == '+':
            result = num1 +  num2
        elif operation == '-':
            result = num1 -  num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно!")
                return
            result = num1 / num2
        elif operation == "**":
            result = num1 ** num2
        else:
            print("Ошибка: неизвестная операция.")
            return

        print(f"Результат: {result}")

    except ValueError:
        print(f"Ошибка: вы ввели буквы вместо чисел!")

if __name__ == "__main__":
    main()
