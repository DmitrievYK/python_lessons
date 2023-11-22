'''Напишсать генератор словарей где ключ - буква, значение - цифра'''
import string, random

# def sortByAlphabet(inputStr): # Функция сортировки по первому элементу для алфовитной сортировки
#         return inputStr[0]

def generate_dict(length_dict):
    values_dict = [] # пустой список значений с длиннной равной длине length_dict
    keys_dict = [] # пустой список ключей с длинной равной дилне length_dict
    for i in range(0, length_dict): # создание случайных букв
        if length_dict <= 26: # проверка заданного числа и количества букв в алфавите
            if __name__ == '__main__':
                keys_dict.append(random.choice(string.ascii_letters)) # добавляем в список букву
            print(keys_dict)
        elif length_dict % 26 == 0: # Если делиться без остатка на 26 - пример 52
            amount_of_occurrences_of_the_alphabet = length_dict / 26 # счетчик сколько символов нужно для обеспечения введенной длины (до 26 - 1 символ, 52 - 2 символа)
            #print(amount_of_occurrences_of_the_alphabet)
    keys_dict.sort() # сортировка букв в алфавитном порядке - ключ первый символ списка (key = sortByAlphabet - нужен для функции sortByAlphabet)4
    return keys_dict



length_dict = int(input('длина словоря, введите цифру: ')) # Длина словаря в цифре

a = generate_dict(length_dict)
print(a)
