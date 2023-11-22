# sp = [88,77, True, 9.99, "Hello", 'world']
# sp2 = [1, 2]
# print(sp + sp2)

# for item in sp:
#     print(item)
# for i in range (len(sp)):
#     print(sp[i])
# for i,value in enumerate(sp):
#     print(i, value)
# print(78 in sp)

# t1 = tuple(sp)
# print(t1)
# t1[0] = 45

# d = {"Ваня": 4654654, "Вася": 45646477}
# d["Сергей"] = 11111
# print(d)
# print(d.keys())
# print(d.values())
# for key, value in d.items():
#     print(key, value)

# s = {77,777,777,777,1,2,3}
# s.add(1000)
# s.discard(11)
# print(s)


# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

numbers = [1, 1, 2, 0, 11, 11, -1, 3, 4, 4]

print(len(set(numbers)))

