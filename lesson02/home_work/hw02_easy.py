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

# ФИО Дунаев В.Г.
# были проблемы с кодировкой и для терминала помогло:
## -*- coding: utf-8 -*-
## !/usr/bin/env python

# так как фрукты могут состоять из оного, двух и более слов то введем их через запятую
string_fruit=input("Введите название фруктов через запятую. После ввода нажмите Enter"+'\n')
#проводим зачистку нашей строки удаляем двойные пробелы два раза для тогной гарантии
#заменяем все возможные вариации написания запятой и пробела на обычную запятую без знака
#а потом сплитуем
string_fruit=string_fruit.replace("  ",' ').replace("  ",' ').replace(" ,",',').replace(" , ",',').replace(", ",',')
list_fruit=string_fruit.split(',')
out_string=""
for i in range(0,len(list_fruit)):
    out_string=out_string+str(i+1)+". {}"+'\n'
print(out_string.format(*list_fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

string_things1=input("Введите элементы 1 списка через запятую. После ввода нажмите Enter"+'\n')
string_things1=string_things1.replace("  ",' ').replace("  ",' ').replace(" ,",',').replace(" , ",',').replace(", ",',')
list_things1=string_things1.split(',')

string_things2=input("Введите элементы 2 списка через запятую. После ввода нажмите Enter"+'\n')
string_things2=string_things2.replace("  ",' ').replace("  ",' ').replace(" ,",',').replace(" , ",',').replace(", ",',')
list_things2=string_things2.split(',')

print("Было")
out_string=""
for i in range(0,len(list_things1)):
    out_string=out_string+str(i+1)+". {}"+'\n'
print(out_string.format(*list_things1))

list_intersect=set(list_things1).intersection(list_things2)
list_things3=set(list_things1).difference(list_intersect)

print("Стало")
out_string=""
for i in range(0,len(list_things3)):
    out_string=out_string+str(i+1)+". {}"+'\n'
print(out_string.format(*list_things3))


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

string_chisel=input("Введите элементы списка через запятую. После ввода нажмите Enter"+'\n')
string_chisel=string_chisel.replace("  ",' ').replace("  ",' ').replace(" ,",',').replace(" , ",',').replace(", ",',').replace(" ",'')
list_chisel=string_chisel.split(',')
list_chisel_new=list_chisel
print("Исходный лист")
print(list_chisel_new)
for i in range(0,len(list_chisel)):
    if list_chisel[i].isdigit():
        if float(list_chisel[i])%2!=0:
            list_chisel_new[i]=int(list_chisel[i])*2
        else:
            if float(list_chisel[i])%4!=0:
                list_chisel_new[i] = float(list_chisel[i]) / 4
            else:
                list_chisel_new[i] = int(int(list_chisel[i]) / 4)
    # для отрицательных отрежем 1 символ - знак для проверки на число ли это
    elif list_chisel[i][1:].isdigit():
        if float(list_chisel[i])%2!=0:
            list_chisel_new[i]=int(list_chisel[i])*2
        else:
            if float(list_chisel[i])%4!=0:
                list_chisel_new[i] = float(list_chisel[i]) / 4
            else:
                list_chisel_new[i] = int(int(list_chisel[i]) / 4)
    else:
        print("ВНИМАНИЕ: элемент под номером "+str(i+1)+" это не число или не целое число")
        list_chisel_new[i]="-это не целое или не число-"
print("Ответ")
print(list_chisel_new)
