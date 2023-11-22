import random

#получить список квадратов нечетных значений списка на входе
def get_square_even(sp):
    result = []
    for item in sp:
        if item % 2: #проверка на нечетность
            result.append(item**2)
    return result



print(sp := [random.randint(1,10) for _ in range(7)] )
print(get_square_even(sp))
print( [ item**2 for item in sp if item % 2 ] )
print( [ item**2 if item % 2 else 0 for item in sp ] )