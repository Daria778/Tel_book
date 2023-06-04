import view
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

def watch_names():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split(" ")[0])

def sort_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_birthday():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key = lambda x: x[3])
    with open("db.txt", "w") as file:
        file.writelines(data)

def delete(data):
    with open("db.txt", "r") as file:
        res = file.readlines()
        for i in range(len(res)):
            if data in res[i]:
                res.pop(i)
        with open("db.txt", "w") as file:
            file.writelines(res)

def rename(data):
    with open("db.txt", "r") as file:
        res = file.readlines()
        for i in range(len(res)):
            if data in res[i]:
                res.pop(i)
                k = view.lol_man()
                res.insert(i, k)
        with open("db.txt", "w") as file:
            file.writelines(res)