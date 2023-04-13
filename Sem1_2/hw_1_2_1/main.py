
heads, tails = 0, 0
coins = int(input("Введите количество монет: "))

for _ in range(coins):
    coin = input("Орел (1) или решка (0)? ")
    if coin == "1": heads += 1
    else: tails += 1
    

print(f"Надо перевернуть орлов - {heads}" if heads < tails else f"Надо перевернуть решек - {tails}")