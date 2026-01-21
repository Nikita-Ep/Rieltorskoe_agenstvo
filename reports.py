# Генерация отчетов

from apartment import shell_sort


def report_full_list(apartments):
#       сортировка по комнатам (убывание), затем по цене (возрастание).

    def key1(apt):
        return (-apt.rooms, apt.price)
    
    sorted_apt = shell_sort(apartments, key1)
    print(f"Отчёт 1: Полный список ({len(sorted_apt)} квартир)")
    print("Сортировка: комнаты ↓, цена ↑")
    return sorted_apt


def report_by_rooms(apartments, rooms):
#       Сортировка этаж (возр), этажность дома (возр), цена (убыв)

    filtered = []
    for apt in apartments:
        if apt.rooms == rooms:
            filtered.append(apt)
    
    if not filtered:
        print(f"Отчёт 2: Квартир с {rooms} комнатами не найдено")
        return []
    
    def key2(apt):
        return (apt.floor, apt.total_floors, -apt.price)
    
    sorted_apt = shell_sort(filtered, key2)
    print(f"Отчёт 2: Квартиры с {rooms} комнатами ({len(sorted_apt)} квартир)")
    print("Сортировка: этаж ↑, этажность дома ↑, цена ↓")
    return sorted_apt


def report_by_price_range(apartments, n1, n2):
# Сортировка цена (убыв), общая площадь (возр)

    if n1 > n2:
        n1, n2 = n2, n1
    
    filtered = []
    for apt in apartments:
        if n1 <= apt.price <= n2:
            filtered.append(apt)
    
    if not filtered:
        print(f"Отчёт 3: Квартир в диапазоне {n1:,.0f} - {n2:,.0f} руб. не найдено")
        return []
    
    def key3(apt):
        return (-apt.price, apt.total_area)
    
    sorted_apt = shell_sort(filtered, key3)
    print(f"Отчёт 3: Квартиры в ценовом диапазоне ({len(sorted_apt)} квартир)")
    print(f"Диапазон: {n1:,.0f} - {n2:,.0f} руб.")
    print("Сортировка: цена ↓, общая площадь ↑")
    return sorted_apt
