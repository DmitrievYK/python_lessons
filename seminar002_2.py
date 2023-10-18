# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

#Var 1
# a = int(input('Введите натуральное число а: '))

# fibArray = [0, 1]

# while a > fibArray[-1]:
#     fibArray.append(fibArray[-1] + fibArray[-2])

# if a == fibArray[-1]:
#     print(len(fibArray))
# else:
#     print('-1')

# Var 2    
# a = int(input('Введите натуральное число а: '))

# fibArray = [0, 1]

# while a > fibArray[-1]:
#     fibArray.append(fibArray[-1] + fibArray[-2])

# if a == fibArray[-1]:
#     print(len(fibArray))

# elif a - fibArray[-2] < fibArray[-1] - a:
#     print(fibArray[-2])

# elif a - fibArray[-2] == fibArray[-1] - a:
#     print((fibArray[-1], fibArray[-2]))
    

# else:
#     print(fibArray[-1])

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
A = int(input('Введите натуральное число а: '))
first, second = 0, 1 #первые два числа фибоначи
n = 1 # Начинаем с второго числа (индекс 1)
current = 1

while current < A:
    current = first + second
    #first, second = second, first + second
    second = first
    first = current
    n +=1
if current == A:
    print(n)
else:
    print(-1)

