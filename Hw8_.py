def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_phonebook('phonebook.txt')
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            phone_book = change_number(phone_book, last_name, new_number)
            write_txt('phonebook.txt', phone_book)
            print_phonebook('phonebook.txt')
        elif choice==4:
            lastname=input('lastname ')
            phone_book = (delete_by_lastname(phone_book, lastname))
            write_txt('phonebook.txt', phone_book)
            print_phonebook('phonebook.txt')
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book, number))
        elif choice==6:
            phone_book = add_user(phone_book)
            write_txt('phonebook.txt',phone_book)
            print_phonebook('phonebook.txt')
        choice=show_menu()

def show_menu():
    print('1. Распечатать справочник ',
          '2. Найти телефон по фамилии ',
          '3. Изменить номер телефона ',
          '4. Удалить запись ',
          '5. Найти абонента по номеру телефона ',
          '6. Добавить абонента в справочник ',
          '7. Закончить работу ', sep = '\n')
    choice=int(input("введите команду "))
    return choice
def read_txt(filename):
    phone_book=[]
    fields=['Фамилия','Имя','Телефон','Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields,   line.split(',')))
            phone_book.append(record)
    return phone_book
def write_txt(filename, phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')
def print_phonebook(filename):
    print('Фамилия,Имя,Телефон,Описание\n')
    with open(filename,'r',encoding='utf-8') as prin:
        for line in prin:
            print(line)
    prin.close()
def find_by_lastname(phone_book, fam):
    find_fam = list(filter(lambda x: x['Фамилия'] == fam, phone_book))
    return list(map(lambda x: x, find_fam))
def  change_number(x, y, z):
    for i in range(len(x)):
        if y == x[i]['Фамилия']:
            x1, x2 = 'Телефон', z
            x[i].update({x1: x2})
    return x
def delete_by_lastname(phone_book, fam):
    return list(filter(lambda x: x['Фамилия'] != fam, phone_book))
def find_by_number(phone_book, number):
    find_num = list(filter(lambda x: x['Телефон'] == number, phone_book))
    return list(map(lambda x : x, find_num))
def add_user(phone_book):
    new_str = {}
    fam = input('Фамилия')
    x1, x2 = 'Фамилия', fam
    new_str.update({x1: x2})
    nam = input('Имя')
    x1, x2 = 'Имя', nam
    new_str.update({x1: x2})
    phone = input('Телефон')
    x1, x2 = 'Телефон', phone
    new_str.update({x1: x2})
    comm = input('Описание')
    x1, x2 = 'Описание', comm
    new_str.update({x1: x2})
    phone_book.append(new_str)
    return phone_book

work_with_phonebook()