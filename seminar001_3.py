# на входе целое или вещественное число. Посчитать количество цифр этого числа
# 0,001 ->4
# 0 - > 1
# 100 -> 3

number = float(input('Введите число: '))
result = 0
num = number

while number > 0:
    d = number % 1
    number = number // 10
    
    result += d
print('Количество чисел', result)

