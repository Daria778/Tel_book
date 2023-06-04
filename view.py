def user_input():
    ask = int(input("Выберите ниже:\n 1 - записать человека в телефонную книжку\n 2 - перезаписать человека\n 3 - удалить человека из телефонной книжки\n 4 - найти человека \n 5 - отсортировать телефонную книгу по имени\n 6 - отсортировать телефонную книгу по номеру телефона\n 7 - посмотреть записи\n 8 - выйти\n "))
    return ask

def lol_man():
    surname = str(input("Введите фамилию: "))
    name = str(input("Введите имя: "))
    string = str(input("Введите Отчество: "))
    birthday = input("Введите дату рождения: ")
    tel = input("Введите номер телефона: ")
    data = string + " " + name + " " + surname + " " + birthday + " " + tel + "\n"
    return data
    
# def correct():
#     ans = input("Корректны ли введенные данные?\n")
#     if ans == "да":
#         return 
#     elif ans == "нет":
#         ans = input("Хотите ли вы перезаписать данные?\n")
#         if ans == "да":
#             data = lol_man()
#         else: 
#             pass
#     return data

def search():
    print("Вы хотите найти человека по номеру телефона или по имени?")
    ss = int(input("Выберите:\n 0 - поиск по номеру телефона\n 1 - поиск по имени\n "))
    if ss == 0:
        call = str(input("Введите номер телефона того, кого зотите найти:\n "))
        return call
    elif ss == 1:
        name = str(input("Введите имя того, кого хотите найти:\n "))
        return name

