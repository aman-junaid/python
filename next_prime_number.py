"""
This script returns next prime number on user input
"""

"""The function generates next prime number"""


def getnextprimenum(lastnum):
    while (True):
        b = isnumprime(lastnum)
        if b:
            return lastnum
            break
        else:
            lastnum += 1


""" 
This function checks if the given number is prime or not
"""


def isnumprime(num):
    if num % 2 == 0:
        return False

    for i in range(3, int((num / 2) + 1)):
        if num % i == 0:
            return False
    return True


""" The function takes user input as Y and N """


def getusrinput():
    while True:
        usin = input('Do you want to compute next prime number?? [Y]- To fetch the next Prime Number, [N]- To Quit! ')
        if usin in ('Y', 'N'):
            return usin


""" Wrapper function"""


def main():
    num = 1
    while True:

        usi = getusrinput()
        if 'Y' == usi:
            num = getnextprimenum(num + 1)
            print(f'Next Prime Number is {num}')
        else:
            print('Exiting the script!')
            break


if __name__ == '__main__':
    main()
