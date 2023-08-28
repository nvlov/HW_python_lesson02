def find_numbers(S, P):
    for x in range(1, S):
        y = S - x
        if x * y == P:
            return x, y
    return None

S = int(input("Введите сумму чисел S: "))
P = int(input("Введите произведение чисел P: "))

result = find_numbers(S, P)

if result:
    print("Задуманные числа: ", result)
else:
    print("Числа не найдены")

