# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей
# n = 6 -> 1 4 1  
# n = 24 -> 4 16 4    
# n = 60 -> 10 40 10

n = int(input('Введите количество журавлей '))

Piter = n / 6
Serg = Piter
Katay = (Serg + Piter) * 2

print(int(Piter), int(Katay), int(Serg))

'''Решение от платформы GB'''
# n1 = n // 6
# n2 = n // 6
# n3 = (n // 6) * 4
# print(n1, n3, n2)
