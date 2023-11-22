# def main_cyclr():
#     while True:
#         print("""Доступные команды:          
#               add - добавить контакт 
#               del - удалить контакт
#               import - сохранение в контакты
#               export - загрузка из контактов
#               """)
#         command = str(input('Введите комманду: '))
#         try: 
#             operations_dict[command]
#         except:
#             print('Команда не найдена')
# # Перечень операций в словаре
# operations_dict = {
#                    'add': add_contact(), 
#                    'del': del_contact(),
#                    'import': import_contacts(),
#                    'export': export_contacts()
#                    }   
# main_cyclr()

def add_contact():
    print('Вызвана функция add_contact')

def del_contact():
    print('Вызвана функция del_contact')

def import_contacts():
    print('Вызвана функция import_contacts')

def export_contacts():
    print('Вызвана функция export_contacts')

def main_cyclr():
    while True:
        print("""Доступные команды:
              add - добавить контакт
              del - удалить контакт
              import - сохранение в контакты
              export - загрузка из контактов
              """)
        command = str(input('Введите команду: '))
        operations_dict = {
            'add': add_contact(), 
            'del': del_contact(),
            'import': import_contacts(),
            'export': export_contacts()
            }

        if command in operations_dict:
            operations_dict[command]
        else:
            print('Команда не найдена')

main_cyclr()