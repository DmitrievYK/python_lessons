# задача 1 сложная необязательная
# Посчитать сумму цифр любого целого или вещественного числа,
# число вводит пользователь.
# Через строку решать нельзя.

from decimal import Decimal
number = Decimal(input('Введите число: '))
number = abs(number) # возвращаем положительное число

#Счетчик цифр
count = 0

# Разделяем число на целую часть и дробную
number_base = int(number)
number_tail = number - number_base

if number_base == 0: # c нулевой целой частью добавляет к счетчику чисел + 1
     count += 1

# Цифры целой части
while number_base != 0:
    number_base //= 10 # удаление целой части - приведение к нулю
    count += 1
    

# Цифры дробной части
while number_tail != 0:
    number_tail = number_tail * 10 # выводим в целое число
    number_tail = number_tail - int(number_tail) # удаляем целую часть - приведение к нулю
    count += 1

print(count)