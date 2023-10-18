# i = 0
# while i < 10:
#     print(i)
#     i += 1


# while True:
#     print(i)
#     i += 1
#     if i == 20:
#         break

# for i in (48, True, 8.11):
#     print(i)

# for k in range(1, 11, 2):
#     print(k)

# print(k)


# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

a = int(input('Введите натуральное число а: '))

res = 1
counter = 2

while counter <= a:
    res *= counter
    counter +=1

print(f'{a}! = {res}')

# a = int(input('Input a: '))
# res = 1
# counter = 1
# while counter <= a:
#     res *= counter
#     counter += 1