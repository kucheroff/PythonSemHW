# Задача 2: Найдите сумму цифр трехзначного числа.

import os

def getNumSum(n):
    summ = 0

    while n > 0 :
        summ += n % 10
        n //= 10
    return summ


os.system('cls')
num = int(input('Введите цеоле число: '))
print(getNumSum(num))
