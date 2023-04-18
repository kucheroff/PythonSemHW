n = int(input("Введите кол-во элементов массива: "))

my_list = list()
count = 0

for i in range(n):
    my_list.append(int(input(f"Введите элемент {i+1}-й массива: ")))

x = int(input("Введите число для подсчета: "))

for item in my_list:
    if item == x: count += 1

print(f"Цифра {x} встречается в массиве чисел {count} раз.")
