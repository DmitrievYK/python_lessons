# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = 5

def get_trunumber(n, div):
    if n % div == 0:
        return False
    if div * div > n:
        return True
    return get_trunumber(n, div + 1)

print(get_trunumber(n, 2))


# def easy(n, divisor):
    
#     if n % divisor == 0:
#         return False
#     if divisor*divisor > n:
#         return True
#     return easy(n, divisor + 1)

# print (easy(11, 2))
