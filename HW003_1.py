# Требуется вычислить, сколько раз встречается
# некоторое число k в массиве list_1.
# Найдите количество и выведите его.
list_1 = [1, 2, 1, 4, 5, 1, 7, 1]
k = 3
# list_1 = [2, 4, 1, 6, 8, 2, 9, 3, 2, 5]
# k = 2
# 1
count = 0
for i in range(0, len(list_1)):
    #print(list_1[i])
    if list_1[i] == k:
        count += 1
print(count)


# i = 0
# while i < len(list_1):
#     print(list_1[i])
#     i += 1