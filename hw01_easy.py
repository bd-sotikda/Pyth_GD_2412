
__author__ = 'Беляев Д.Ю.'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
a = int(input("Введите любое целое число: "))
print("Вы ввели число -", a)
print("Выводим числа по разрядам, начиная с младшего разряда")
while a != 0:
    print(a % 10)
    a = int(a/10)
    
print("Работа программы завершена")

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
a = int(input("Введите первое значение, a = "))
b = int(input("Введите второе значение, b = "))
c = a + b
b = c - b
a = c - b
print("Мы поменяли значения местами")
print("Первое значение - ", a)
print("Второе значение - ", b)

print("Работа программы завершена")
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

a = int(input("Введите Ваш возраст: "))
if a >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

print("Работа программы завершена")
