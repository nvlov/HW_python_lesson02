# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.



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

