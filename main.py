import sys
from file_handling import load_apartments, save_report
from reports import report_full_list, report_by_rooms, report_by_price_range


def clear_screen():
    print("\n" * 50)


def print_header():
    print("=" * 70)
    print("Риэлтерское агентство - Управление базой данных квартир".center(70))
    print("=" * 70)


def print_menu():
    print("\n" + "-" * 70)
    print("ГЛАВНОЕ МЕНЮ".center(70))
    print("-" * 70)
    print("1. Загрузить базу квартир из файла")
    print("2. Полный список квартир (сортировка: комнаты ↓, цена ↑)")
    print("3. Список квартир с заданным количеством комнат")
    print("4. Список квартир в ценовом диапазоне")
    print("5. Сохранить текущий отчёт в файл")
    print("0. Выход")
    print("-" * 70)


def print_separator():
    print("-" * 70)


def get_int_input(prompt, min_val=None, max_val=None):
#           Безопасный ввод целого числа с проверкой диапазона
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Ошибка: введите значение")
                continue
                
            value = int(value)
            
            if min_val is not None and value < min_val:
                print(f"Ошибка: значение должно быть не меньше {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Ошибка: значение должно быть не больше {max_val}")
                continue
                
            return value
        except ValueError:
            print("Ошибка: введите целое число")


def get_float_input(prompt):
#       Безопасный ввод вещественного числа
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Ошибка: введите значение")
                continue
            return float(value)
        except ValueError:
            print("Ошибка: введите число")


def print_apartments(apartments, title=""):
    if not apartments:
        print("Нет данных для отображения")
        return
    
    if title:
        print(f"\n{title}")
        print_separator()
    
    print(f"Найдено квартир: {len(apartments)}")
    print_separator()
    
    for i, apt in enumerate(apartments, 1):
        print(f"{i:3}. {apt}")
    
    print_separator()


def main():
    apartments = []
    current_report = []
    current_report_name = ""
    
    while True:
        clear_screen()
        print_header()
        
        if apartments:
            print(f"\nЗагружено квартир: {len(apartments)}")
            if current_report_name:
                print(f"Текущий отчёт: {current_report_name}")
            print_separator()
        
        print_menu()
        
        choice = input("\nВыберите пункт меню (0-5): ").strip()
        
        if choice == "1":
            clear_screen()
            print_header()
            print("\n" + "=" * 70)
            print("ЗАГРУЗКА БАЗЫ ДАННЫХ".center(70))
            print("=" * 70)
            
            filename = input("Введите имя файла с данными: ").strip()
            
            if not filename:
                print("Ошибка: имя файла не может быть пустым")
                input("\nНажмите Enter для продолжения...")
                continue
            
            loaded = load_apartments(filename)
            if loaded is not None:
                apartments = loaded
                current_report = apartments
                current_report_name = "Полная база данных"
            input("\nНажмите Enter для продолжения...")
        
        elif choice == "2":
            if not apartments:
                print("Ошибка: сначала загрузите базу данных (пункт 1)")
                input("\nНажмите Enter для продолжения...")
                continue
            
            clear_screen()
            print_header()
            current_report = report_full_list(apartments)
            current_report_name = "Полный список квартир"
            
            print_separator()
            print_apartments(current_report)
            input("\nНажмите Enter для продолжения...")
        
        elif choice == "3":
            if not apartments:
                print("Ошибка: сначала загрузите базу данных (пункт 1)")
                input("\nНажмите Enter для продолжения...")
                continue
            
            clear_screen()
            print_header()
            print("\n" + "=" * 70)
            print("ПОИСК КВАРТИР ПО КОЛИЧЕСТВУ КОМНАТ".center(70))
            print("=" * 70)
            
            rooms = get_int_input("Введите количество комнат: ", 1, 10)
            
            clear_screen()
            print_header()
            current_report = report_by_rooms(apartments, rooms)
            current_report_name = f"Квартиры с {rooms} комнатами"
            
            if current_report:
                print_separator()
                print_apartments(current_report)
            input("\nНажмите Enter для продолжения...")
        
        elif choice == "4":
            if not apartments:
                print("Ошибка: сначала загрузите базу данных (пункт 1)")
                input("\nНажмите Enter для продолжения...")
                continue
            
            clear_screen()
            print_header()
            print("\n" + "=" * 70)
            print("ПОИСК КВАРТИР ПО ЦЕНЕ".center(70))
            print("=" * 70)
            
            print("Введите ценовой диапазон:")
            n1 = get_float_input("Минимальная цена (руб.): ")
            n2 = get_float_input("Максимальная цена (руб.): ")
            
            if n1 < 0 or n2 < 0:
                print("Ошибка: цена не может быть отрицательной")
                input("\nНажмите Enter для продолжения...")
                continue
            
            clear_screen()
            print_header()
            current_report = report_by_price_range(apartments, n1, n2)
            current_report_name = f"Квартиры в ценовом диапазоне {n1:,.0f} - {n2:,.0f} руб."
            
            if current_report:
                print_separator()
                print_apartments(current_report)
            input("\nНажмите Enter для продолжения...")
        
        elif choice == "5":
            if not current_report:
                print("Ошибка: нет данных для сохранения. Сначала сгенерируйте отчёт")
                input("\nНажмите Enter для продолжения...")
                continue
            
            clear_screen()
            print_header()
            print("\n" + "=" * 70)
            print("СОХРАНЕНИЕ ОТЧЁТА".center(70))
            print("=" * 70)
            print(f"Текущий отчёт: {current_report_name}")
            print(f"Количество записей: {len(current_report)}")
            print_separator()
            
            filename = input("Введите имя файла для сохранения: ").strip()
            
            if not filename:
                print("Ошибка: имя файла не может быть пустым")
                input("\nНажмите Enter для продолжения...")
                continue
            
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            save_report(filename, current_report, current_report_name)
            input("\nНажмите Enter для продолжения...")
        
        elif choice == "0":
            clear_screen()
            print_header()
            print("\n" + "=" * 70)
            print("ВЫХОД ИЗ ПРОГРАММЫ".center(70))
            print("=" * 70)
            print("Спасибо за использование программы!")
            print("До свидания!")
            print("=" * 70)
            sys.exit(0)
        
        else:
            print("Ошибка: неверный выбор. Введите число от 0 до 5")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
