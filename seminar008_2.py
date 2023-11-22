# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Операции - импорта из functions.py

#from random import *
import json

# Адресная книга загрузка
phonebook = {}
try:
    with open("contact.json", "r", encoding="utf-8") as ct:
        phonebook = json.load(ct)
    print("Автоматическая загрузка адресной книги прошла успешно")
except:
    phonebook = {}
    
    # phonebook = {"дядя Ваня": {'phones': [1212121, 5555555],
    #                        'email': '777@mail.com', 'birthday': '10.10.1990'},
    #         "Кирил":{'phones':[4567878], 'birthday': '21.02.1988'}
    #         }


# phonebook = {"дядя Ваня": {'phones': [1212121, 5555555],
#                            'email': '777@mail.com', 'birthday': '10.10.1990'},
#             "Кирил":{'phones':[4567878], 'birthday': '21.02.1988'}
#             }


# Добавить контакт
def add_contact(phonebook):
    name= input('Введите имя: ')
    phones = input('Введите номер телефона: ')
    email = input('Введите email: ')
    birthday = input('Введите день рождения: ')
    contact = {"phones": phones, "email": email, "birthday": birthday}
    phonebook[name] = contact
    # with open("contact.json", "w", encoding="utf-8") as ct:
    #     ct.write(json.dump(phonebook, ensure_ascii=False))
    # print("Добавлен контакт в адресную книгу")

# Удалить контакт
def del_contact(phonebook):
    name = input('Введите имя контакта чтоб удалить: ')
    del phonebook[name]
    print(f'Контакт с именем {name} удален!')


# Поиск контакта
# def find_contact(phonebook):
#     search_field = input('Введите по какому параметру ведем поиск: Имя, Телефон, Почта ?')
#     print()
#     if search_field == 'Имя':
#         name = input('Введите имя: ')
#         if name in phonebook:
#             return print(phonebook[name])
#         else:
#             return print('Контакт не найден в телефонной книге!')
#     elif search_field == 'Телефон':
#         phones = int(input('Введите номер телефона: '))
#         if phones in phonebook[name]['phones']:
#             return print(phonebook[name])
#         else:
#             return print('Контакт не найден в телефонной книге!')
#     elif search_field == 'Почта':
#         email = input('Введите почту: ')
#         if email in phonebook[email]:
#             return print(phonebook[name]['email'])
#         else:
#             return print('Контакт не найден!')
#     else:
#         print('Введите правильную команду: Имя, Телефон, Почта')

def find_contact(phonebook):
    search_field = input('Введите по какому параметру ведем поиск: Имя, Телефон, Почта ? ')
    print()
    if search_field == 'Имя':
        name = input('Введите имя: ')
        if name in phonebook:
            return print(phonebook[name])
        else:
            return print('Контакт не найден в телефонной книге!')
    elif search_field == 'Телефон':
        phones = input('Введите номер телефона: ')
        for name, contact_info in phonebook.items():
            if 'phones' in contact_info and phones in contact_info['phones']:
                return print(contact_info)
            return print('Контакт не найден в телефонной книге!')
    elif search_field == 'Почта':
        email = input('Введите почту: ')
        for name, contact_info in phonebook.items():
            if 'email' in contact_info and contact_info['email'] == email:
                return print(contact_info)
            return print('Контакт не найден!')
# Показать все контакты
def show_all(phonebook):
    print(phonebook)

#Изменить контакт
def edit_contact():
    pass
    # def edit_phone(name, n_phone = 0):
    #     new_phone = int(input(f'Введите номер телефона {n_phone} для контакта {name}: '))
    #     phonebook[name]['phones'][n_phone] = new_phone
    #     return
        # field = input('''Выберите контакт:
        #           Телефон
        #           Email
        #           Дата рождения
        #           '''
        #           )
    
# Закрыть приложение
# def close_app():
#     pass
    # print("Завершение работы телефонного справочника, возвращайтесь к нам еще")
    

# Сохранить(импорт) контакты в файл
def import_contact():
    with open("contact.json", "w", encoding="utf-8") as ct:
        json.dump(phonebook, ct)
    print("Изменения сохранены в адресной книге!")

# Загрузить(экспорт) контакты из файла
def export_contact():
    with open("contact.json", "r", encoding="utf-8") as ct:
        phonebook = json.load(ct)
    print("Загрузка адресной книги прошла успешно!")
    return phonebook

def main_cyclr():
    while True:
        print("""Доступные команды:
               
              add - добавить контакт 
              del - удалить контакт
              find - поиск контакта 
              all - показать все контакты
              close - закрыть приложение 
              edit - изменеть контакт
              import - сохранение в контакты
              export - загрузка из контактов
              """)
        
        command = str(input('Введите комманду: '))
        # operations_dict = {
        #            'add': add_contact(), 
        #            'del': del_contact(), 
        #            'find': find_contact(),
        #            'all': show_all(), 
        #            'edit': edit_contact(),
        #            'close': close_app(),
        #            'import': import_contact(),
        #            'export': export_contact()
        #            }

        
        # if command in operations_dict:
        #     operations_dict[command]
        # else:
        #     print('Команда не найдена')

        # try: 
        #     operations_dict[command]
        
        # except:
        #     print('Команда не найдена')

        # if command == operations_dict['all']:
        #     operations_dict['all']
        if command == 'add':
            add_contact(phonebook)
        elif command == 'del':
            del_contact(phonebook)
        elif command == 'find':
            find_contact(phonebook)
        elif command == 'all':
            show_all(phonebook)
        elif command == 'edit':
            edit_contact()
        elif command == 'import':
            import_contact()
        elif command == 'export':
            export_contact()
        elif command == 'close':
            print("Завершение работы телефонного справочника, возвращайтесь к нам еще")
            break
        else:
            print('Команда не найдена')

# Перечень операций в словаре
 
main_cyclr()




    





'''Код второй группы'''
# import json

# def save():
#     with open('phone_book.json', "w", encoding='utf-8') as file:
#         file.write(json.dumps(phone_book, ensure_ascii=False))
#     print("Данные сохранены")


# contacts = {}

# while True:
#     command = input("Введите команду: ")
#     if command == "show":
#         print(contacts)
#     elif command == "find":
#         contact_name = input("Введите имя: ")
#         print(contacts[contact_name])
#     elif command == "del":
#         contact_name = input("Введите имя: ")
#         del contacts[contact_name]
#         print("Запись успешно удалена")
#     elif command == "save":
#         save()
#     elif command == "add":
#         contact_name = input("Введите имя: ")
#         phones = input("Введите номера телефонов через запятую: ").split(",")
#         email = input("Введите email через запятую: ").split(",")
#         contact = {
#             'phones': phones,
#             'email': email,
#             'birthday': input("Введите день рождения: ")
#         }
#         contacts[contact_name] = contact
#         print("Контакт успешно добавлен")

#     elif command == "exit":
#         break