import math

n = int(input("Введите кол-во элементов массива: "))
my_list = list()

for i in range(n):
    my_list.append(int(input(f"Введите элемент {i+1}-й массива: ")))

x = int(input("Введите число для поиска ближайшего к нему: "))

min_diff = abs(x - my_list[0])
num_near = list[0]

for i in range(1, len(my_list)):
    new_diff = abs(x-my_list[i])
    if new_diff  < min_diff:
        min_diff = new_diff
        num_near = my_list[i]
    
print(f"Ближайшим к числу {x} в массиве чисел является число {num_near}.")