def hello(name):
    return "Hello, " + name

def bye(name):
    return name + ", bye bye"

def create_phrase(func):
    name = input("Введите свое имя ")
    print("Это функция высшего порядка")
    return func(name)

def create_two_phrase(funcs):
    name = input("Введите свое имя ")
    print("Это функция высшего порядка")
    res = ""
    for func in funcs:
        res += func(name) + "\n"
    return res

# funcs = (hello, bye)
# # print(create_phrase(hello))
# # print(create_phrase(bye))
# print(create_two_phrase(funcs))

def calc_power(degree):
    def power(base):
        return base ** degree
    return power

# print(calc_power(3) (2))
# cube = calc_power(3)
# square = calc_power(2)

# degrees = [calc_power(i) for i in range(10)]

# # print(cube(5))
# # print(square(12))
# for i in range(len(degrees)):
#     print(degrees[i] (2))

# square = lambda x: x**2

sp = [1,2,3,4,5,6,7]
# print(*map(lambda x: x**2, sp))
# print(list(map(lambda x: x**2 if x%2 else  0, sp)))
# print(*filter(lambda x: x%2, sp))
# print(*filter(lambda x: x>88, sp))
calculator = {  "+": lambda x,y: x+y,
                "-": lambda x,y: x-y,
                "/": lambda x,y: x/y,
                "*": lambda x,y: x*y
             }
x, op, y = input("Введите арифметическое выражение ").split()
print(f"Результат равен {calculator[op] (int(x), int(y)) }")

sp2 = ["Вася", "Ваня"]
print(list(zip(sp,sp2)))

