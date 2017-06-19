import sys
import os
from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits
import sqlobject as sq

from model import *

def main():
    args = sys.argv[1:]
    db_filename = args[0]
    open_db(db_filename)

    for i in list(range(10)):
        first_name = choice(ascii_uppercase)+''.join(choice(ascii_lowercase) for i in range(randint(4, 9)))
        last_name = choice(ascii_uppercase)+''.join(choice(ascii_lowercase) for i in range(randint(4, 9)))
        pesel = ''.join(choice(digits) for i in range(14))
        print(first_name, last_name, pesel)
        o = Owners(first_name=first_name, last_name=last_name, pesel=pesel)
        for i in range(randint(1,4)):
            brand = choice(ascii_uppercase)+''.join(choice(ascii_lowercase) for i in range(randint(4, 9)))
            model = choice(ascii_uppercase)+''.join(choice(ascii_lowercase) for i in range(randint(4, 9)))
            number = ''.join(choice(ascii_uppercase) for i in range(2))+''.join(choice(digits) for i in range(5))
            print("   ", brand, model, number)
            c = Cars(brand=brand, model=model, number=number, owners=o)













if __name__ == '__main__':
    main()
