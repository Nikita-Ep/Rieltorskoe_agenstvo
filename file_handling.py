# Модуль для чтения и записи файлов с данными квартир.
from apartment import Apartment

def load_apartments(filename):

    apartments = []
    try:
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        
        if not lines:
            print("Файл пустой!")
            return None
            
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = [part.strip() for part in line.split(',')]
            if len(parts) != 10:
                print(f"Ошибка в строке {line_num}: неверное количество полей")
                continue
            
            try:
                apt = Apartment(
                    street=parts[0],
                    house=int(parts[1]),
                    apartment=int(parts[2]),
                    rooms=int(parts[3]),
                    total_area=float(parts[4]),
                    living_area=float(parts[5]),
                    floor=int(parts[6]),
                    total_floors=int(parts[7]),
                    owner=parts[8],
                    price=float(parts[9])
                )
                apartments.append(apt)
            except ValueError as e:
                print(f"Ошибка в строке {line_num}: {e}")
                continue
                
        if apartments:
            print(f"Успешно загружено {len(apartments)} записей")
        else:
            print("Не удалось загрузить ни одной записи")
            return None
            
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    
    return apartments


def save_report(filename, apartments, report_name=""):
    try:
        file = open(filename, 'w', encoding='utf-8')
        
        if report_name:
            file.write(f"{report_name}\n")
            file.write("=" * 80 + "\n\n")
        
        for i, apt in enumerate(apartments, 1):
            file.write(f"{i:3}. {str(apt)}\n")
        
        file.close()
        
        print(f"Отчёт сохранён в файл: {filename}")
        print(f"Сохранено записей: {len(apartments)}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении отчёта: {e}")
        return False
