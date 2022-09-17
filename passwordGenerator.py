#making a password generator which make the stronf password for you

import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    #print(st)
    s2 = string.ascii_uppercase
    #print(sy)
    s3 = string.digits
    #print(su)
    s4 = string.punctuation
    #print(si)
    passlength = int(input("enter pasword length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("your password is: ")
    print("".join(s[0:passlength]))