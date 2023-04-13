import math

c = int(input("Введите сумму двух чисел: "))
d = int(input("Введите произведение двух чисел: "))

a = (-c + math.sqrt(c**2-4*d)) / -2
b = c - a

print(f"Загаданные числа {int(a)} и {int(b)}.")
