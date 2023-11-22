# Задача №43. 
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3 Вывод: 2

# import random

# print(sp := [random.randint(1, 10) for _ in range(7)])

# count = 0

# for i in set(sp):
#     count += sp.count(i) // 2
# print(count)

# print(sum([sp.count(i) // 2 for i in set(sp)]))

import random

print(sp := [random.randint(1, 10) for _ in range(7)])

count = 0

for i in set(sp):
    count += sp.count(i) // 2

print(sum([sp.count(i) // 2 for i in set(sp)]))
print(count)