# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
#

test1 = ["Задача 1:",
         "Дан список фруктов.",
         "Напишите программу, выводящую фрукты в виде нумерованного списка,",
         "выровненного по правой стороне."]
for t in test1:
    print(t)

fruits = input("Введите список любимых фруктов: ").split(',')

#fruits = ['яблоко', 'груша', 'апельсин', 'банан']
i = 0
while i < len(fruits):
    print('{0}   {1:>10}'.format(i+1, fruits[i]))
    i += 1

print('Задача по выводу списка фруктов завершена')
print('-'*80)

test2 = ["Задача 2:",
         "Даны два произвольные списка",
         "Удалите из первого списка элементы, присутствующие во втором списке"]
for t in test2:
    print(t)

list1 = input("Введите произвольный список №1: ").split(',')
list2 = input("Введите произвольный список №2: ").split(',')
list_all = list1[:]
#list_all = set(list1 + list2)
#print("Итоговый непересекающийся список: ", list_all)

for el in list1:
    if el in list2:
        list_all.remove(el)
        break
    else:
        continue
    
print("Итоговый список: ", list_all)
print("Первоначальный список: ", list1)

print('Задача по удалению из элементов второго списка из первого завершена')
print('-'*80)

test3 = ["Задача 3:",
         "Дан произвольный список из целых чисел.",
         "Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:",
         "если элемент кратен двум, то разделить его на 4,",
         "если не кратен, то умножить на два"]
for t in test3:
    print(t)

list1 = input("Введите произвольные целые числа: ").split(',')
new_list = []
for d in list1:
    if int(d) % 2 == 0:
        new_d = int(d) / 4
        new_list.append(new_d)
    else:
        new_d = int(d) * 2
        new_list.append(new_d)
        
print("Исходный список: ", list1)
print("Новый список:", new_list)


print('Задача по формированию нового списка завершена')
print('-'*80)

