#  Сортировка Шелла

class Apartment:
    def __init__(self, street, house, apartment, rooms, total_area, 
                 living_area, floor, total_floors, owner, price):
        self.street = street
        self.house = house
        self.apartment = apartment
        self.rooms = rooms
        self.total_area = total_area
        self.living_area = living_area
        self.floor = floor
        self.total_floors = total_floors
        self.owner = owner
        self.price = price

    def __str__(self):
        price_str = f"{self.price:,.0f}".replace(',', ' ')
        return (f"{self.street}, д.{self.house}, кв.{self.apartment}, "
                f"{self.rooms}к, {self.total_area:.1f}м², "
                f"жилая {self.living_area:.1f}м², этаж {self.floor}/{self.total_floors}, "
                f"владелец: {self.owner}, цена: {price_str} руб.")


def shell_sort(apartments, key_func):
#       Сортировка Шелла с использованием key_func для получения кортежа ключей
    if not apartments:
        return []
    
    arr = apartments[:]  # Создаем копию списка
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            while j >= gap and key_func(arr[j - gap]) > key_func(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr
