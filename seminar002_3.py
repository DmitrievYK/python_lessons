# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# from random import randint

# days = int(input('Количество дней: '))
# current_warm_days = 0
# max_warm_days = 0

# for i in range(days):
#     #temperat = randint(-50, 50)
#     temperat = int(input('температура дня: '))
#     #print(temperat)
#     if temperat > 0:
#         current_warm_days += 1 
#     else:
#         if current_warm_days > max_warm_days:
#             max_warm_days = current_warm_days
#         current_warm_days = 0
# print(max_warm_days)


# ВТОРОЙ ВАРИАНТ
# n = int(input('Общее количество дней:'))

# count = 0
# res = 0

# for i in range(n):    
#     temperature = int(input('Среднесуточная температура в соответствующий день:'))
#     if temperature > 0:
#         count +=1
#         if res < count:
#             res = count
#     if temperature < 0:
#         count = 0

# print(f'Самая длинная оттепель длилась {res} дней')

# ТРЕТИЙ ВАРИАНТ ПРАВИЛЬНЫЙ
n = int(input('Общее количество дней:'))

cur_warm = 0
longest_warm = 0

for i in range(n):    
    temperature = int(input('Среднесуточная температура в соответствующий день:'))
    if temperature > 0:
        cur_warm +=1
        if longest_warm < cur_warm:
            longest_warm = cur_warm
    if temperature < 0:
        cur_warm = 0

print(f'Самая длинная оттепель длилась {longest_warm} дней')