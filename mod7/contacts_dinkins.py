import csv

names = []
email = []
phone = []

def csvread():
    with open('contacts.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            names.append(row[0])
            email.append(row[1])
            phone.append(row[2])

def csvwrite():
    with open('contacts.csv', 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        filewriter.writerow([name, email, phone])


def csvprint():
    v1 = int(input('Contact number: '))
    v = v1 - 1
    print(names[v])
    print(email[v])
    print(phone[v])

while True:
    csvread()
    csvwrite()
    csvread()
    csvprint()
    break
