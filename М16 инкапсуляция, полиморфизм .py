#ИНКАПСУЛЯЦИЯ

# class Animal:
#     def __init__(self, type_animal, name):
#         self.type_animal = type_animal
#         self.name = name
#
#     def info_name(self):
#         print(f'Я {self.type_animal} по имени {self.name}')
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__('кошка', name)
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кошка мне {self.age}')
#
#     def sound(self):
#         print('Мяу')
#
# class Dog(Animal):
#     size = 'xl'
#     def __init__(self, name, age):
#         super().__init__('собака', name)
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака мне {self.age}')
#
#     def sound(self):
#         print('Гав')
#
#     def __belt(self):
#         print(f'Размер ошейника {self.size}')
#
# cat = Cat('Вася', 3)
# dog = Dog('Альма', 4)
#
# dog._Dog__belt()


# ПОЛИМОРФИЗМ
# class Animal:
#     def __init__(self, type_animal, name):
#         self.type_animal = type_animal
#         self.name = name
#
#     def info_name(self):
#         print(f'Я {self.type_animal} по имени {self.name}')
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__('кошка', name)
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кошка мне {self.age}')
#
#     def sound(self):
#         print('Мяу')
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__('собака', name)
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я собака мне {self.age}')
#
#     def sound(self):
#         print('Гав')
#
# cat = Cat('Вася', 3)
# dog = Dog('Альма', 4)
#
# for animal in (cat, dog):
#     animal.info_name()
#     animal.sound()
#     animal.info()

# name = input('Введите ваше имя ')
# age = input('Введите ваш возраст ')
# print(name, age)

# num = int(input('Введите число '))
# if num % 2 == 0:
#     print('Четное')
# else:
#_______________________________________________________________
# #Сортировка при вводе 0, выход из цикла и формирования списка.
# num = int(input('Введите целое число '))         #4
# data = []
# while num != 0:                                  # data = [4, 5 ...]
#     data.append(num)
#     num = int(input('Введите целое число '))     # 5
# # data.sort()
# print(data)
# #_____________________________________________________________
##______________________________________________________________
# data = [2, 3, 4]
# data.append(5)
# print(data)
##______________________________________________________________

