# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


names = ['Сергей', 'Петр', 'Иван', 'Начальник']
salarys = ['100000', '200000', '400000', '600000']

def string_for_table(name, salary):
    result_dic = dict(zip(names, salarys))
    return result_dic

def table_to_string(line):
    names.append(line.split(' ')[0])
    salarys.append(int(line.split(' ')[2])*0.87)

def output_table(x):
    for key, value in x.items():
#        if line.split(' ')[2] < '500000':
        print('{} - {}'.format(key, value))

a = string_for_table(names, salarys)

with open('salary.txt', 'w', encoding='utf-8') as file_salary:
    for key, value in a.items():
        file_salary.write('{} - {} \n'.format(key, value))


with open('salary.txt', 'r') as file_salary:
    for line in file_salary:
        names = []
        salarys = []
        table_to_string(line)
        b = string_for_table(names, salarys)
    output_table(b)
    
