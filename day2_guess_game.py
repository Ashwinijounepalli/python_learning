#Python picks a number (let’s say 7)
#You guess the number
#Python tells you if your guess is correct or not

x=int(input("enter number: "))
number=7
if (x>7):
    print(f"oh no, {x} Your guessing more than max digit!")
elif (x<7):
    print(f"oh no, {x} youre guessing less than min digitt!")
else:
    print(f"hey {x} ,youre right!")