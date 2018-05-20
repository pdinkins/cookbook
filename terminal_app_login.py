from time import sleep
import os

login = False
run = True
titlestat = [0]

if login == False:
    titlestat.clear()
    titlestat.append(2)


#### Classes
class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        import datetime
        return datetime.datetime.now()

#### define the class instances
admin1 = Admin('admin', 'password')
dt1 = DateTime()


def title():
    # running titlebar
    print('=' * 80)
    print('PYTHOS\t\t', dt1.dt())
    print('=' * 80)
    
    # subtitle
    if titlestat[0] == 0:
        print('\n\t\tLOGIN')
        print('=' * 80)
    
    elif titlestat[0] == 1:
        print('\n\t\tLOGIN FAILED')
        print('=' * 80)
    
    elif titlestat[0] == 2:
        print('\n\t\tNODE_ADMIN')
        print('=' * 80)




def clear():
    try:
        os.system('cls')
    
    except:
        
        import platform
        ops = platform.system()
        if ops == 'Darwin':
            os.system('clear')

def refresh_screen():
    clear()
    title()




####### LOGIN SEQUENCE #######
while login:
    title()
    usn = input('username: ')
    if usn != admin1.username:
        titlestat.clear()
        titlestat.append(1)
        refresh_screen()
                
    elif usn == admin1.username:
        titlestat.clear()
        titlestat.append(0)
        refresh_screen()
        pasw = input('password: ')

        if pasw == admin1.password:
            titlestat.clear()
            titlestat.append(2)
            refresh_screen()
            print('You are logging in as ', usn)
            refresh_screen()
            break



# MENU
# displays a menu, user choice, choice function execution.
'''
USE:
    1. import menu
    2. define menu choice functions
    3. define menu dictionary
        {'menu choice label': corresponding function}
    4. menu.initialize_menu(**menu_dictionary, **menutitle)
'''

def initialize_menu(menu_dictionary, menutitle):
    menulist = list(menu_dictionary.keys())
    #menulist = menu_dictionary
    j = 1
    print('\n' + menutitle, '\n')
    for i in range(0,len(menulist)):
        print(j,'-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)


def choose_from_menu(menulist, menu_dictionary):
    try:
        try:
            menuchoice = int(input('\nMenu Choice:  '))
        except EOFError:
            return
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')


def quit_menu():
    quit()

def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    index = 0
    tsizevar = 0
    '''
    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            print(os.path.join(root, file))

        for name in dirs:
            print(os.path.join(root, name))
    '''
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    print('=' * 80)
    for root, dirs, files in os.walk(pathname):
        for file in files:
            pathname = os.path.join(root, file)
            size = os.path.getsize(pathname)
            tsizevar += size
            #print(index, '\t\t', size, '\t\t', pathname)
            index += 1

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata


    '''
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dirsize = os.path.getsize(dirpath)
            print(index, '\t\t', dirsize, '\t\t', dirpath)
            index += 1
    '''     



def rootfile_list():
    spath = 'C:/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    try:
        for i in range(0, len(root_dict)):
                path = 'C:/' + root_dict[i]
                subroot = os.listdir(path)
                print('\t', path)
                
                for j in range(0, len(subroot)):
                    print('\t\t',j, subroot[j])

    except (TypeError, NotADirectoryError):
        #print('type error')
        pass
    input('rootfile_list>\t')
    return rootfilelist


def rootfile_list_2():
    spath = 'C:/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    
    for i in range(0, len(rootfilelist)):
        print('\n', i, spath, rootfilelist[i])

    input('rootfile_list>\t')
    return rootfilelist
        


mm = {
    'Root file system list': rootfile_list,
    '2': rootfile_list_2,
    'rfs': rfsm
}
######## APP INTERFACE ########
while run:
    refresh_screen()
    command = input('>')
    if command == '0':
        refresh_screen()
        print('LOGING OUT OF THE MATRIX')
        clear()
        break

    elif command == '1':
        refresh_screen()              
        initialize_menu(mm, 'ROOT FILE SYSTEM MAIN MENU')

    elif command == '2':
        path = input('path >\t')
        rfs(path)
        command = input('>')

