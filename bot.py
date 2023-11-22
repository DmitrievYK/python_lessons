# Бот на локалке, следующим шагом запуск его в ТГ
# ctrl + c - завершение программы

from random import *
import json

films = []

def save():
    with open("films.json", "w", encoding="utf-8") as fh: # fh это псевдоним(переменная) чтобы не писать полностью film.json
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша фильмотека былас успешно сохранена в файле films.json")

# def load():
#     with open("films.json", "r", encoding="utf-8") as fh:
#         films = json.load(fh)
#     print("Фильмотека была успешно загружена")

try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена")
    #load()

except:
    #films = []
    films.append("Матрица")
    films.append("Солярис")
    films.append("Властелин колец")
    films.append("Техасская резня бензопилой")
    films.append("Санта-барбара")

while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот-фильмотека начал свою работу")
    elif command =="/stop":
        print("Бот остановил свою работу. Заходите еще, будем вам рады!")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f = input("Введите название фильма: ")
        films.append(f)
        print(f"фильм \"{f}\" добавлен в коллекцию")
    elif command == "/help":
        print("Перечень комманд добавить")
    elif command == "/del":
        d = input("Введите название просмотренного фильма чтобы удалить из списка: ")
        '''
        if d in films:
            films.remove(d)
            print(f"Фильм \"{d}\" удален из фильмотеки")
        else:
            print("Такого фильма нет в списке")
            '''
        try: # Попытайся если нет то иди в except
            films.remove(d)
            print(f"Фильм \"{d}\" удален из фильмотеки")
        except:
            print("Такого фильма нет в списке")
    elif command == "/rand":
        # rnd = randint(0, len(films - 1))
        # print("Слепой жребий выдает фильм: " + films[rnd])
        print("Слепой жребий выдает фильм: " + choice(films))
    elif command == "/save": # Сохранение в файл film.json через функцию(метод) save (13-ая строка)
        save()
    elif command == "/load":
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека была успешно загружена")
        #load()
    else:
        print("Неопознаная команда. Просьба изучить мануал через /help")