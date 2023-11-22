# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Примечание: числа S и P задавать не нужно, они будут передаваться в тестах.
# В результате вы должны вывести все возможные пары чисел X и Y через пробел, такие что X <= Y.

# На входе: s = 12 p = 27
# На выходе: 3 9



''' Решаем перебором'''
# s = 12 
# p = 27

# for x in range(1,s // 2, +1):
#     y = s - x
#     if x <= y and x*y == p:
#         print(x, y)

'''Решение через дискриминант'''
import math

s = 4 
p = 4

a = 1
b = -s
c = p

discriminant = float(b*b - 4*a*c)
#print('discr', discriminant)

if discriminant <= 0:
    x = int(-b / 2 * a)
    #print(x)
else:
    x = int((-b - math.sqrt(discriminant)) / 2 * a)
    #print(x)

y = s - x

print(x, y)


# x + y = s

# x * y = p

# x ** 2 - s * x + p = 0

'''Решение от платформы GB (Перебор в два цикла с условиями сборка в список)'''
# solutions = []
# for i in range(1, 1001):
#     for j in range(1, 1001):
#         if s == i + j and p == i * j:
#             solutions.append((min(i, j), max(i, j)))
# solutions = list(set(solutions))

# for solution in solutions:
#     print(solution[0], solution[1])