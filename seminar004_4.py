# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

'''Задача №29. Решение в группах
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)'''


'''Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)'''


# Пользователь вводит натуральное k. 
# Надо сформировать многочлен такой степени, 
# где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random

def polynomial(k: int):
    coeff = [random.randint(-10, 10) for _ in range (k + 1)]
    output_str = ""
    for i in range(len(coeff)):
        if i == 0 and abs(coeff[0]) == 1:
            if coeff[0] > 0:
                output_str += f"x^{k-i} + "
            else:
                output_str += f"-x^{k-i} + "
        elif coeff[i] != 0:
            output_str += f"{coeff[i]}*x^{k-i} + "
    return output_str.replace('+ -', '- ').replace('*x^0', ' ').replace('*x^1', 'x ').replace(' 1*', ' ')[: -3] + ' = 0'

k = 4
print(polynomial(k))


'''Недоработанная конструкция'''
# import random

# def polynomial (k: int):
#     coeff = [random.randint(-10,10) for _ in range(k+1)]
#     output_str = "" 
#     for i in range(len(coeff)):
#         if coeff[i] != 0:
#             output_str += f"{coeff[i]}*x^{k-i} + "
#     return output_str.replace('+ -', '- ').replace('*x^0', '').replace('x^1 ', 'x ').replace(' 1*', ' ')[:-3] + " = 0"

# print(polynomial(4))

'''Доработанный код на семинаре'''

# import random

# def polynomial (k: int):
#     coeff = [random.randint(-10,10) for _ in range(k+1)]
#     output_str = "" 
#     for i in range(len(coeff)):
#         if i==0 and abs(coeff[0]) == 1:
#             if coeff[0] > 0:
#                 output_str += f"x^{k-i} + "
#             else:
#                 output_str += f"-x^{k-i} + "
#         elif coeff[i] != 0:
                        
#             output_str += f"{coeff[i]}*x^{k-i} + "
#     return output_str.replace('+ -', '- ').replace('*x^0', '').replace('x^1 ', 'x ').replace(' 1*', ' ')[:-3] + " = 0"

# print(polynomial(4))