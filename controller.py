import view
import database

def main():
    while True:
        ask = view.user_input()
        if ask == 1:
           data = view.lol_man()
           database.ggg(data)
        elif ask == 4:
            ss = view.search()
            database.sr(ss)
        elif ask == 5:
            database.sort_name()
        elif ask == 6:
            database.sort_birthday()
        elif ask == 7:
            database.watch()
        elif ask == 8:
            break
main()        



