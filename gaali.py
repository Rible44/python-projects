#this program show a random gaali to you :)

import random
from plyer import notification


name =  input("enter your name : ")

slang = [
    "deer",
    "beaver",
    "cow",
    "ladchatte",
    "g@ndu",
    "laude",
    "bhosdk",
    "madarchod",
    "chuttd ke madarchod"
]

random.shuffle(slang)
print("according to me you are")
print(random.choice(slang))