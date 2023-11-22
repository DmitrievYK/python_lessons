# Задача №41
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# ввод:
# N - 5 
# 1 2 3 4 5 
# вывод: - 0 (1)

# ввод:
# N - 5 
# 1 5 1 5 1
# вывод: - 2


# import random

# print( sp := [random.randint(1,10) for _ in range(7)])
# #sp = [1, 2, 3, 4, 5]
# count = 0
# for i in range(len(sp)):
#     #print(sp[i - 1], sp[i], sp[(i + 1) % len(sp)])
#     if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i]:
#         count += 1
# print(count)
# print(sum([1 for i in range(len(sp)) if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i]]))
# print([1 for i in range(len(sp)) if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i]])

import random

print(sp := [random.randint(1, 10) for _ in range(7)])
# sp = [1, 2, 3, 4, 5]
count = 0
for i in range(len(sp)):
    # print(sp[i - 1], sp[i], sp[(i + 1) % len(sp)])
    if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i]:
        count += 1

print(count)
print(sum([1 for i in range(len(sp)) if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i]]))
print([1 if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i] else 0 for i in range(len(sp))])
print([True if sp[i - 1] < sp[i] and sp[(i + 1) % len(sp)] < sp[i] else False for i in range(len(sp))])