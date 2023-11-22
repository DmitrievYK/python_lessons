# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод: 300  Вывод: 220 284

# def sum_devisiors(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum

# k = int(input('Введите число: '))
# result = []

# for i in range(1, k + 1):
#     y = sum_devisiors(i)
#     if sum_devisiors(y) == i and i < y:
#         result.append((i, y))

# print(result)

# print([(i, sum_devisiors(i)) for i in range(1, k + 1)] if sum_devisiors(sum_devisiors(i)) == i and i < sum_devisiors(i))

def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

k = int(input("Введите число: "))
result = []

for i in range(1, k + 1):
    y = sum_divisors(i)
    if sum_divisors(y) == i and i < y:
        result.append((i, y))

print([(i, sum_divisors(i)) for i in range(1, k + 1) if sum_divisors(sum_divisors(i)) == i and i < sum_divisors(i)])
print(result)

'''numpy.array - библиотеки нумпай, работа для аналитиков работа с большим количеством данных'''