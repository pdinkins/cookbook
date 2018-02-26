import csv

names = []
email = []
phone = []


def csvread():
    with open('contacts.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            names.append(row[0])
            email.append(row[1])
            phone.append(row[2])
          

def csvwrite():
    with open('contacts.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        filewriter.writerow([name, email, phone])


def view():
    v1 = int(input('\nContact number: '))
    v = v1 - 1
    print('\nName: ', names[v])
    print('Email: ', email[v])
    print('Phone #: ', phone[v])


def llist():
    namelen = len(names)
    listnum = 1
    for i in range(0, namelen):
        print(listnum, '. ', names[i])
        listnum += 1


def listclear():
    names.clear()
    email.clear()
    phone.clear()


def add():
    csvwrite()
    listclear()
    csvread()
    

def delete():
    file = open('contacts.csv', 'r')
    lines = file.readlines()
    file.close()
    delnum = int(input('Contact number to delete: '))
    delnum -= 1
    del lines[delnum]
    open('contacts.csv', 'w').writelines(lines)
    listclear()
    csvread()


def command_menu():
    print('COMMAND MENU')
    menuchoices = [
        'list - Display all contacts',
        'view - View a contact',
        'add - Add a contact',
        'del - Delete a contact',
        'exit - Exit program'
        ]
    size = len(menuchoices)
    for i in range(0, size):
        print(menuchoices[i])


command_dict = {
    'list': llist,
    'view': view,
    'add': add,
    'del': delete
    }


while True:
    print('Contact Manager\n')
    csvread()
    command_menu()
    break    

while True:
    try:
        command = input('\nCommand: ')
        if command == 'exit':
            print('Bye')
            break
        else:
            command_dict[command]()
    except KeyError:
        print("\n****Invalid Command****\n")
