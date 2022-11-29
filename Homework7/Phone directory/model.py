import controller

def menuItem(data):
    if data == '1':
        viewContacts()
    elif data == '2':
        addContacts()
    elif data == '3':
        searchContacts()
    elif data == 'q':
        exit()
    else:
        print('Выбрано неверное значение, повторите ввод!')
        controller.Start()


def viewContacts():
    data = open('contacts.txt', 'r', encoding="utf=8")
    viewing = data.read()
    data.close
    print(viewing)


def addContacts():
    data = open('contacts.txt', 'a', encoding="utf=8")
    name = input('Введите -  Имя и номер телефона: ')
    data.writelines(f"{name} \n")
    data.close

       
def searchContacts():
    data = open('contacts.txt', 'r', encoding="utf=8")
    name = data.read()
    name = name.split('\n')
    data.close
    search = input("Введите имя: ")
    for i in range(len(name)):
        result = name[i]
        if search == str(result[0: len(search)]):
            print(result)
        
