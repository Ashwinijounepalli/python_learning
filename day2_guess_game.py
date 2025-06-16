#Python picks a number (let’s say 7)
#You guess the number
#Python tells you if your guess is correct or not
'''
x=int(input("enter number: "))
number=7
if (x>7):
    print(f"oh no, {x} Your guessing more than correct number!")
elif (x<7):
    print(f"oh no, {x} youre guessing less than correct number!")
else:
    print(f"hey {x} ,youre right!")
'''

#random number
import random
x=int(input("enter number: "))
number=random.randint(1, 10)

if (x>number):
    print(f"oh no, {x} Your guessing more than correct number!")
elif (x<number):
    print(f"oh no, {x} youre guessing less than correct number!")
else:
    print(f"hey {x} ,youre right!")

print(f"rand num is {number}")
