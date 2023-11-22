# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст

# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
# как, например, у операции умножения.

# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9

# def print_operation_table(operation, num_rows, num_columns):
#     a = [[operation] * num_rows for x in range(num_columns)]
#     for i in range(num_rows):
#         for j in range(num_columns):
#             #a[i][j] = operation
#             print(a[i][j], end=' ')

'''Первый вариант решения'''
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#     # Вывод нумерации столбцов
#         header = " ".join(str(i) for i in range(1, num_columns + 1))
#         print(header)
#         for i in range(2, num_rows + 1): # задаем для каждого i-ого элемента начиная с 1 до указанного числа 
#             print(f"{i}")
#             for j in range(2, num_columns + 1): # задаем для каждого j-ого элемента начиная с 1 до указанного числа
#                 result = operation(i, j) # берем значения i и j элемента по которым идем двумя циклами и выполняем лямбда урованиене -> lambda x, y: x * y
#                 print(result, end=' ')
#             print()


# print_operation_table(lambda x, y: x / y, 4, 4)
'''Попробовать'''

# def printOperationTable(f, h, w):
#   for i in range(1, h+1):
#     print(*(f(i, k) for k in range(1, w+1)))

'''Верно считает'''
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#     # Вывод нумерации столбцов
#         header = " ".join(str(i) for i in range(1, num_columns + 1))
#         print(header)
#     # Вывод значений
#         for i in range(2, num_rows + 1):
#             row_str = str(i) + " "
#             for j in range(2, num_columns + 1):
#                 row_str += str(operation(i, j)) + " "
#             print(row_str)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    else:
    # Вывод нумерации столбцов
        header = "\t".join(str(i) for i in range(1, num_columns + 1))
        print(header)
    # Вывод значений
        for i in range(2, num_rows + 1):
            row_str = str(i)
            for j in range(2, num_columns + 1):
                row_str += f"\t{operation(i, j)}"
                #row_str += operation(i, j)
            print(row_str)

print_operation_table(lambda x, y: x - y, 5, 5)

'''Ответы'''
# print_operation_table(lambda x, y: x / y, 4, 4)
# Ожидаемый ответ:

# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0

# Ваш ответ:

# 1.0 0.5 0.3333333333333333 0.25 
# 2.0 1.0 0.6666666666666666 0.5 
# 3.0 1.5 1.0 0.75 
# 4.0 2.0 1.3333333333333333 1.0

# print_operation_table(lambda x, y: x - y, 5, 5)
# Ожидаемый ответ:

# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0

# Ваш ответ:

# 0 -1 -2 -3 -4 
# 1 0 -1 -2 -3 
# 2 1 0 -1 -2 
# 3 2 1 0 -1 
# 4 3 2 1 0

# print_operation_table(lambda x, y: x + y, 4, 4)
# Ожидаемый ответ:

# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

# Ваш ответ:

# 2 3 4 5 
# 3 4 5 6 
# 4 5 6 7 
# 5 6 7 8

# print_operation_table(lambda x, y: x * y, 3, 3)
# Ожидаемый ответ:

# 1 2 3
# 2 4 6
# 3 6 9

# Ваш ответ:

# 1 2 3 
# 2 4 6 
# 3 6 9

'''Второй вариант решения'''
# def print_operation_table(operation, num_rows, num_columns):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[f'{x:>3}' for x in i])
        
# print_operation_table(lambda x, y: x * y, 6, 6)
# print_operation_table(lambda x, y: x / y, 4, 4)