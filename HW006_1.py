# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.

# На входе:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# На выходе:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19
'''Первое решение - через два списка, сравниваются между собой и выводятся те индексы где есть совпадения '''
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#list_1 = [0, 0, -2, 1]
min_number = 0
max_number = 10
print(list_1)
#count = -1
#list_2 = [i for i in range(min_number, max_number + 1)] # Генератор списка с началом от мин до макс

# for item in list_1:
#     count += 1
#     if item in list_2:
#         print(count)

'''Второе решение - применение функции enumerate и генератора списка с заданными условиями иф между макс и мин'''
list_2 = [index for index, value in enumerate(list_1) if min_number <= value <= max_number]
for x in list_2:
    print(x)

'''Третье решение от платформы GB - проходимся по списку от нуля по всей длине списка и если попадаем в диапазон то печатаем индекс'''
# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)
