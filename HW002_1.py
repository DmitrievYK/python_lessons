# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть,
# чтобы все монетки лежали одной и той же стороной вверх.

# Входные данные:
# На вход программе подается список coins, 
# где coins[i] равно 0, если i-я монетка лежит гербом вверх, 
# и равно 1, если i-я монетка лежит решкой вверх. 
# Размер списка не превышает 1000 элементов.

# Выходные данные:
# Программа должна вывести одно целое число - 
# минимальное количество монеток, которые нужно перевернуть.

# coins = [0, 1, 0, 1, 1, 0]
# На выходе:  3

'''Нужно посчитать все нули и единицы и сравнить кого меньше'''
coins = [0, 1, 0, 1, 1, 0]
coins_len = len(coins)
count_zero = 0
count_unity = 0
for i in range(0, coins_len):
    if coins[i] == 0:
        count_zero += 1
        #print('ноль - ', count_zero)
    else:
        count_unity += 1
        #print('один - ', count_unity)
if count_zero < count_unity:
    print('zero - ', count_zero)
else: print('unity', count_unity)

'''Решение от платформы GB'''
# coins = [0, 1, 0, 1, 1, 0]
# count_zero = 0
# count_one = 0

# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1

# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)