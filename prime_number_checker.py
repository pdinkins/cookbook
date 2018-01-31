# prime number checker
# parker dinkins


# define a function
def print_factors(x):
    # This function takes a number and prints the factors

    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            # print('x=', x)
    print(x, 'is not a prime number')


def prime_checker():
    try:
        #a = int in range(0,5000)
        a = int(input("Enter number between 0 and 5000: ")) #in range(0, 5000)

        if a is False:
            prime_checker()
            #print('****ERROR****')
            #print('Enter a number between 0 and 5000 please\n')
            #prime_checker()

        k = 0
        for i in range(2, a // 3):
            if a % i == 0:
                k = k + 1

        if k <= 0:
            print('The factors of your number are:')
            print('1')
            print(a, 'is a PRIME number')

        else:
            print_factors(x=a)

    except ValueError:
        print('****Invalid*Input****\nPlease enter a number\n')


run = True
run1 = True

while run:
    prime_checker()
    break

while run1:
    option = input('quit [y/n]: ')
    if option == 'y':
        break
    elif option == 'n':
        prime_checker()
    else:
        print('Please enter [y/n]')
