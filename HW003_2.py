# Требуется найти в массиве list_1 
# самый близкий по величине элемент 
# к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 2, 1, 1, 2, 0]
k = 6
# 5
'''Второй вариант решения'''
# closest = list_1[0] # Предполагаем, что первый элемент является ближайшим к k

# for num in list_1: # num идет как число в списке
#     print(num)
#     if abs(num - k) < abs(closest - k):
#         closest = num

#print("Ближайший элемент к", k, ":", closest)

'''Решение для автотеста'''
closest = list_1[0] # Предполагаем, что первый элемент является ближайшим к k

for num in list_1: # num идет как число в списке
    if abs(num - k) < abs(closest - k):
        closest = num

print(closest)

'''Первый вариант решения'''
# temp = 0 
# min = k
# count = 0
# box = 0

# for i in range(0, len(list_1)):
#     #print(list_1[i])
#     temp = abs(k - list_1[i])
#     count += 1
#     if temp < min:
#         min = temp
#         box = count
# print(list_1[box - 1])


'''решение от платформы GB'''

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


