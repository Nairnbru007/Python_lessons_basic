# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass

def my_round(number, ndigits) -> float:
    if int(number*(10**(ndigits+1))) % 10 >=5:
        out = (int(number*(10**ndigits)) + 1) / (10**ndigits)
    else:
        out= int(number*(10**ndigits)) / (10**ndigits)
    return out

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass

def lucky_ticket(ticket_number) -> bool:
    if len(str(ticket_number))==6 and str(ticket_number).isdigit():
        firs=ticket_number//1000
        second=ticket_number%1000
        sum1 = firs%10 + firs//10%10 + firs//100%10
        sum2 = second%10 + second//10%10 + second//100%10
        if sum1 == sum2:
            return True
        else:
            return False
    else:
        pass

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
