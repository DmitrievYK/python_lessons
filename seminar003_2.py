# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
k = 7

for i in range(k):
    temp = numbers.pop()
    numbers.insert(0, temp)

print(numbers)


numbers = [1, 2, 3, 4, 5]
k = 7

# k = k % len(numbers)
# print(numbers[-k:]+numbers[:-k])