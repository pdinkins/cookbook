# prime number checker
# parker dinkins


def print_factors(x):
    # This function takes a number and prints the factors
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
    print(x, 'is not a prime number')


def prime_checker():
    try:

        a = int(input("Enter number between 0 and 5000: "))
        k = 0
        if a > 5000:
            print('please enter a number between 0 - 5000')
            del a

        elif a < 5000:
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
    option = input('\nWould you like to run the program again? [y/n]: ').lower()
    if option == 'n':
        break
    elif option == 'y':
        prime_checker()
    else:
        print('\nPlease enter [y/n]')
