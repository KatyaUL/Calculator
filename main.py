import db_manager

"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic #Импортируем наш новый модуль

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("=== Модульный Калькулятор v4.0 (со статистикой и поиском) ===")

    db_manager.init_db()

    while True:
        print("\n--- Меню ---")
        print("1. Выполнить вычисление")
        print("2. Показать историю (последние 10)")
        print("3. Очистить историю")
        print("4. Показать статистику")
        print("5. Поиск по истории")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            perform_calculation()
        elif choice == '2':
            show_history()
        elif choice == '3':
            db_manager.clear_history()
            print("История очищена.")
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            search_history()
        else:
            print("Неверный выбор. Попробуйте снова.")

def perform_calculation():
    """Выполняет вычисление и сохраняет результат в БД."""
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /, **): ")

    try:

        if operation == '+':
            result = calc_logic.add(num1, num2)
        elif operation == '-':
            result = calc_logic.subtract(num1, num2)
        elif operation == '*':
            result = calc_logic.multiply(num1, num2)
        elif operation == '/':
            result = calc_logic.divide(num1, num2)
        elif operation == '**':
            result = calc_logic.power(num1, num2)
        else:
            print("Неизвестная операция!")
            return

        expression = f"{num1} {operation} {num2}"
        db_manager.save_record(expression, result)
        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")

def show_history():
    """Показывает последние 10 записей из истории."""
    history = db_manager.get_history(10)

    if not history:
        print("История пуста.")
        return

    print("\n--- История вычислений ---")
    for record in history:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")

def show_statistics():
    """Показывает статистику вычислений. """
    stat = db_manager.get_statistics()
    count, avg, max_val, min_val = stat
    if count == 0:
        print("История пуста, статистики нет.")
        return
    print("\n---- Статистика вычислений ---")
    print(f"Общее количество: {count}")
    print(f"Среднее значение: {avg:.2f}")
    print(f"Максимальное значение: {max_val}")
    print(f"Минимально значение: {min_val}")

def search_history():
    """Ищет записи по ключевому слову."""
    keyword = input("Введите ключевое слово для поиска (например, число): ")
    records = db_manager.search_history(keyword)
    if not records:
        print("Ничего не найдено.")
        return
    print(f"\n--- Результаты поиска по '{keyword}' ---")
    for record in records:
        print(f"[{record[3]}] {record[1]} = {record[2]}")

if __name__ == "__main__":
    main()
