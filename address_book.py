import pandas as pd
a = pd.DataFrame(columns=["ФИО", "Адрес", "Телефон", "Дата рождения"])
c = 0
while True:
    print("Адресная книга")
    print("1-Показать все записи")
    print("2-Добавить запись")
    print("3-Удалить запись")
    print("4-Изменить запись")
    print("5-Выход")   
    b = input("Выберите действие: ")
    if b == "1":
        if len(a) == 0:
            print("Адресная книга пуста.")
        else:
            print(a)
    elif b == "2":
        fio = input("Введите ФИО: ")
        adres = input("Введите адрес: ")
        num = input("Введите телефон: ")
        birth = input("Введите дату рождения: ")
        c += 1
        a.loc[c] = [fio, adres, num, birth]
        print("Запись добавлена")
    elif b == "3":
        if len(a) == 0:
            print("Адресная строка пуста")
        else:
            print(a)
            d = int(input("Введите номер записи, чтобы удалить: "))
            if d in a.index:
                a = a.drop(d)
                print("Запись удалена")
            else:
                print("Такой записи нет")
    elif b == "4":
        if len(a) == 0:
            print("Адресная книга пуста")
        else:
            print(a)
            d = int(input("Введите номер записи, чтобы изменить: "))
            if d in a.index:
                print("Оставьте поле пустым, если не будете менять")
                for column in a.columns:
                    g = input(f"Новое значение для поля {column}: ")
                    if g != "":
                        a.loc[d, column] = g
                print("Запись изменена")
            else:
                print("Такой записи нет")
    elif b == "5":
        print("До свидания")
        break
    else:
        print("Введите другое значение")