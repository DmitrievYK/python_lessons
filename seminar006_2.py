# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# ввод:
# N - > 7
# 3 1 3 4 2 4 12

# M - > 6 (4)
# 3 3 2 12         

# вывод: 3 3 2 12
import random
print( sp1 := [random.randint(1,10) for _ in range(7)])
print( sp2 := [random.randint(1,10) for _ in range(4)])

#print(result := [sp1 & sp2])
result = []
for item in sp1:
    if item not in set(sp2):
        result.append(item)
print(result)

print([item for item in sp1 if item not in set(sp2)])


