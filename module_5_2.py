# Цель: применить на практике знания о классах, объектах и их атрибутах.

'''
Задача "Developer - не только разработчик
'''

# Реализуйте класс House
class House:
    def __init__(self,name, number_of_floors): # self.name - имя, self.number_of_floors - кол-во этажей
        self.name = name
        self.number_of_floors = number_of_floors
        self.new_floor = 1  # единица принята как первый этаж
    # go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.   
    def go_to(self, new_floor):
        # Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует"
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
             # выводит на экран(в консоль) значения от 1 до new_floor(включительно)
            for floor in range(1, new_floor + 1):
                print(floor)
            self.new_floor = new_floor
            print(f'Вы остановились на {self.new_floor} этаже')



# Исходные данные:
h1 = House('ЖК Горский', 18)
print(h1.name, h1.number_of_floors)
h1.go_to(5)

h2 = House('ЖК Домик в деревне', 2)
print(h2.name, h2.number_of_floors)
h2.go_to(10)

h3 = House('ЖК Эльбрус', 30)
print(h3.name, h3.number_of_floors)
h3.go_to(3)

h4 = House('ЖК Желтый', 4)
print(h4.name, h4.number_of_floors)
h3.go_to(-3)
