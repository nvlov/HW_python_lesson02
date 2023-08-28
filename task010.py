# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.



coins = input("Введите список монеток через пробел: ").split()

count_heads = 0
count_tails = 0

for coin in coins:
    if coin == "1":
        count_heads += 1
    else:
        count_tails += 1

min_flips = min(count_heads, count_tails)
print("Минимальное количество монет для переворота:", min_flips)