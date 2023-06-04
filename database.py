def ggg(data):
    with open("db.txt", "a") as file:
        file.writelines(data)
    print("Запись была обновлена")

def sr(data):
    with open("db.txt", "r") as file:
        res = file.readlines()
        flag = False
        for i in res:
            if data in i:
                print(i)
                flag = True
        if flag == False:
            print("Такого контакта нет или он записан по-другому")

def watch():
    with open("db.txt", "r") as file:
        print(file.read())

def sort_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_birthday():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key = lambda x: x[4])
    with open("db.txt", "w") as file:
        file.writelines(data)