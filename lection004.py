# def f(x):
#     return x ** 2
# print(f(2))

# def f(x):
#     return x ** 2
# g = f
# print(f(4)) # 16
# print(g(4)) # 16

# def calc1(x):
#     return x + 10
# print(calc1(10)) # 20

# def calc2(x):
#     return x * 10
# def math(op, x):
#     print(op, x)
# math(calc2, 10) # 100

# def sum(x, y):
#     return x + y
# def mylt(x, y):
#     return x * y
# def calc(op, a, b):
#     print(op(a, b))
# calc(mylt, 4, 5) # 20

# def calc(op, a, b):
#     print(op(a, b))
# def sum(x, y):
#     return x + y
# f = sum
# calc(f, 4, 5) # 9

'''Применение лямбда'''
# def sum(x, y):
#     return x + y
# # ⇔ (равносильно)
# sum = lambda x, y: x + y

# def calc(op, a, b):
#      print(op(a, b))
# calc(lambda x, y: x + y, 4, 5)



'''Задача 1'''
# В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

'''Через лямбда'''
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

'''Функция map'''

# list_1 = [x for x in range (1,20)]
# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# data = '1 2 3 5 8 15 23 38'.split()
# print(data)       # ['1', '2', '3', '5', '8', '15', '23', '38']
# data = list(map(int, input().split()))

'''map() позволит избавиться от функции select'''

# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''Функция filter'''
# Функция filter() применяет указанную функцию к каждому элементу
# итерируемого объекта и возвращает итератор с теми объектами, для которых
# функция вернула True.

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]

'''filter() позволит избавиться от функции where, которую мы писали ранее'''

# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''Функция zip'''
# Функция zip() применяется к набору итерируемых объектов и
# возвращает итератор с кортежами из элементов входных данных

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)      # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip () пробегает по минимальному входящему набору
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

'''Функция enumerate'''
# Функция enumerate() применяется к итерируемому объекту и
# возвращает новый итератор с кортежами из индекса и элементов входных
# данных

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]


'''Файловая работа в питоне'''
# Варианты режима (мод):
# 1. a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл
# будет создан и в него начнётся запись.
# 2. r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует,
# программа выдаст ошибку.
# 3. w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не
# существует.
# Миксованные режимы:
# 4. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 5. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку

# 1. Режим a

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# data.close() — используется для закрытия файла, чтобы разорвать
# подключение файловой переменной с файлом на диске.
# exit() — позволяет не выполнять код, прописанный после этой команды в
# скрипте.
# В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# При повторном выполнении скрипта redbluedreenredbluedreen — добавление
# в существующий файл, а не перезапись файлов.

# with open('file.txt', 'w') as data:
# data.write('line 1\n')
# data.write('line 2\n')

# Режим r

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()


'''Модуль os'''
# Модуль os предоставляет множество функций для работы с операционной
# системой, причем их поведение, как правило, не зависит от ОС, поэтому программы
# остаются переносимыми.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:

# import os

# Познакомимся с базовыми функциями данного модуля:
# функция os.chdir(path) - смена текущей директории.

# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')

# функция os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# функция os.path - является вложенным модулем в модуль os и реализует некоторые
# полезные функции для работы с путями, такие как: -> os.path.basename(path) - базовое имя пути

# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) # 'main.py'

# функция os.path.abspath(path) - возвращает нормализованный абсолютный путь.

# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

'''Модуль shutil'''
# Модуль shutil содержит набор функций высокого уровня для обработки файлов,
# групп файлов, и папок. В частности, доступные здесь функции позволяют
# копировать, перемещать и удалять файлы и папки. Часто используется вместе с
# модулем os.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:
# import shutil
# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path
# должен указывать на директорию, а не на символическую ссылку.

