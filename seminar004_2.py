# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


def get_symb(some_str: str) -> str:
    result = ""
    input_str = some_str.split()
    count_dict = {}

    for item in input_str:
        if item in count_dict:
            count_dict[item] += 1
            result += f"{item}_{count_dict[item]} "
        else:
            count_dict[item] = 0
            result += f"{item} "
    return result

test_str = "a a a b c a a d c d d"

print(get_symb(test_str))


# def get_symb (some_str: str) -> str:
#     result = "" 
#     input_str = some_str.split()
#     count_dict = {}
    
#     for item in input_str:
#         if item in count_dict:
#             count_dict[item] += 1
#             result += f"{item}_{count_dict[item]} "
#         else:
#             count_dict[item] = 0
#             result += f"{item} "
            
#     return result.strip()


# test_str = "a a a b c a a d c d d"
# print(get_symb(test_str))