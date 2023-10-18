'''Списки'''
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 8]
#print(list_1)

# for i in list_1: #печать значения из списка
#     print(i)

#print(len(list_1)) # печать длины списка

# print(list_1[0])
# print(list_1[3])
# print(list_1[-1]) # Нумерация с конца тоесть 8
# print(list_1[-2]) # Нумерация с конца тоесть 3


# print(list_1)
# list_1.append(8) # Добавление в список нового элемента
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)


# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # удаляем последний элемент списка тоесть 0 и выводит эту переменную
# a = list_1.pop() # мы забрали элемент из списка и присвоили переменной а
# print(a)
# print(list_1)
# print(list_1.pop())
# print(list_1)



# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # Первое число это позиция, второе это само число добавляемое в список
# print(list_1)



# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

'''Множественные присваивания'''

# a, b, c = 1, 2, 3 # значения переменных равны соответствующим значениям

# a, b, c = v # все три числа равны одному

'''Кортежи'''

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)


# Распаковка кортежа
# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# a, b, c = v
# print(a, b, c)


# Выводим значения кортежа
# варинат №1
# t = (1, 2, 3, 5,)

# for i in t:
#     print(i)

# вариант №2
# t = (1, 2, 3, 5,)

# for i in range(len(t)):
#     print(t[i])

'''Работа со словарями'''

# d = {} # фигурные скобки означает что мы создали словарь
# d = dict()

# d['q'] = 'qwerty' # Добавляем значение qwerty по ключу q - если мы запросим q получим кверти
# print(d)

# d['w'] = 'werty' # добавили еще одно значение
# print(d['q']) # вывод значения кверти по ключу q

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():  k - это ключ v - это значение с этим ключем
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

'''Множества'''

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # Добавление в множество нового элемента - но если оно есть уже то оно не добавиться
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray') # А то значение которого нет добавиться, но добавиться не обязательно в конец
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # Удаление значения из множества
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok  - Проверяет значение в множестве если есть то удаляет, а если нет то пропускает
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } - удаляет все элементы из множества
# print(colors) # set()

# q = set() # Создание множества

# Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} - копирование множества а
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объединение множеств но без повторений
# i = a.intersection(b) # i = {8, 2, 5} - пересечение все значения повторяющиеся записываются без повторений
# dl = a.difference(b) # dl = {1, 3} - разница множеств а минус b остаеться только множество а в котором не повторялись значения из b
# dr = b.difference(a) # dr = {13, 21} - разница множества b минус а остаються значения из b
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
#   [2 действие]           [1 действие]

# a = {1, 8, 6}
# b = frozenset(a) # Заморозка множества, чтоб невозможно его было изменить
# print(b)

'''Генерация списка'''
# список
# list_1 = [exp for item in iterable]
# выборка по заданному условию
# list_1 = [exp for item in iterable (if conditional)]

'''Пример использования'''
# Нужно создать список от 1 до 100

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# Применяем генерацию списка

# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# Добавить условие (только чётные числа)

# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]

# Допустим, вы решили создать пары каждому из чисел (кортежи)

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.

# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]
