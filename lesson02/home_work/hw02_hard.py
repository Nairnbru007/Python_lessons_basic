# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
equation = 'y = -12x + 11111140.2121'
x = 2.5
import re
str_equ = re.match(r"y = -(\d+)x \+ (\d+)\.(\d+)", equation)
print(str_equ)
k,b,c=str_equ.groups()
#b=str_equ.group(1)
k=-float(k)
b=float(b+"."+c)
print("k = ",k," b = ",b)
y= k*x + b
print("y = ",y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

import re
import datetime
data=input("Введите дату"+'\n')
data_split=data.split('.')
if len(data_split)!=3:
    print("Дата имеет неверный формат")
    quit()
error=False # Флажок ошибки
# Проверяем год
if data_split[2].isdigit():
    if len(data_split[2])==4:
        if int(data_split[2]) in range(1,9999+1):
            print("год верен")
        else:
            print("формат года не верен (не в диапазоне от 1 до 9999)")
            error=True
    else:
        print("формат года не верен (колличество символов)")
        error=True
else:
    print("В поле год потусторонние символы (не цифры)!")
    error = True
# Проверяем месяц
if data_split[1].isdigit():
    if len(data_split[1])==2:
        if int(data_split[1]) in range(1, 12+1):
            print("месяц верен")
        else:
            print("формат месяца не верен (не в диапазоне от 1 до 12)")
            error = True
    else:
        print("формат месяца не верен (колличество символов)")
        error = True
else:
    print("В поле месяц потусторонние символы (не цифры)!")
    error = True
# Проверяем день
if data_split[0].isdigit():
    if len(data_split[0]) == 2:
        if int(data_split[0]) in range(1, 31+1):
            print("день верен")
        else:
            print("формат дня не верен (не в диапазоне от 1 до 31)")
            error = True
    else:
        print("формат дня не верен (колличество символов)")
        error = True
else:
    print("В поле день потусторонние символы (не цифры)!")
    error = True
if error==False:
    try:
        check_date=datetime.datetime(int(data_split[2]),int(data_split[1]),int(data_split[0]))
    except:
        print("Формат даты верен, но дата не подтверждена в соответствии с Григорианским календарем")
        quit()
    else:
        print("Формат даты верен и дата подтверждена в соответствии с Григорианским календарем")
else:
    print("Итог : Формат даты не верен")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

import re
new_chislo=input("Введите искомую квартиру(целое положительное число > 0 )"+'\n')
if new_chislo.isdigit():
        new_chislo=int(new_chislo)
        if new_chislo == 0:
            print("0 квартиры не существует")
            quit()
else:
    print("Неправильное число или вообще не число")
    quit()
# Рассмотрим последовательность началов блоков 1 2 6 15 31
# При анализе можно заметить, что между ними можно вставить функцию x^2
# (31-15=16=4^2)
# (15-6=9=3^2)
# (6-2=4=2^2)
# (2-1=1=1^2)
# 1 2   6       15          31
# 1 2 4 6 09 12 15 19 23 27 31
#   3 5 7 10 13 16 20 24 28
#       8 11 14 17 21 25 29
#               18 22 26 30
# У каждого i блока i^2 квартир
# 1 блок 1    1 квартира
# 2 блок 2 3  4 квартиры
#        4 5
# итд
# Искомое число в любом случае лежит между двумя началами блоков, нас как раз интерессует
# Nach_blok i < chislo < Nach_blok i+1
# номера этажей начала блока идет так 1 2 4 7 11 возрастающая прогрессия с шагом +1 +2 +3 +4
nabor=[]
nachalo_bloka=1
blok=1
flor_nach_blok=1
nabor.append([nachalo_bloka,blok,flor_nach_blok])
chislo_kv_blok=1
while nachalo_bloka <= new_chislo:
    nachalo_bloka=nachalo_bloka + blok*blok
    flor_nach_blok=flor_nach_blok+1*blok
    blok=blok+1
    nabor.append([nachalo_bloka, blok, flor_nach_blok])
# Нашли начало следующего блока, большего чем число, но нам нужен предыдущий лок, а не следующий
# так как число в нем не лежит, ибо начао блока больше его
current_nabor = nabor[len(nabor)-2]
nachalo_bloka = current_nabor[0]
blok=current_nabor[1]
flor_nach_blok=current_nabor[2]

if blok>1:
    chislo_inblok = (new_chislo - nachalo_bloka + 1)
    if chislo_inblok % blok == 0:
        current_flor = (chislo_inblok//blok -1)+flor_nach_blok
        schet_sleva = chislo_inblok - blok * (chislo_inblok//blok -1)
    else:
        current_flor = (chislo_inblok // blok) + flor_nach_blok
        schet_sleva = chislo_inblok - blok * ((new_chislo - nachalo_bloka + 1) // blok)
else:
    current_flor = ((new_chislo - nachalo_bloka + 1) // blok) + flor_nach_blok - 1
    schet_sleva = (new_chislo - nachalo_bloka + 1) - blok * ((new_chislo - nachalo_bloka + 1) // blok) +1

# print("Квартира " + str(new_chislo) + " лежит в блоке номер " + str(blok)+ " на "+str(current_flor)+" этаже, " + str(schet_sleva) + " слева" )
print(str(current_flor)+" "+str(schet_sleva))
