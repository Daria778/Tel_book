import view
import database

def main():
    while True:
        ask = view.user_input()
        if ask == 1:
           data = view.lol_man()
           database.ggg(data)
        elif ask == 2:
            xx = view.search()
            database.rename(xx)
        elif ask == 3:
            vv = view.search()
            database.delete(vv)
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
            database.watch_names()
        elif ask == 9:
            break
main()        



