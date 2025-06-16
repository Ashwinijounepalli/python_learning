#Asks your name and age
#Says hello
#Tells you how old you'll be after 5 years
# Tell them how old they'll be in 5 years
name=input("Enter Your Name: ")
age=int(input("Enter your age: "))
print("hello")
print(f"hello {name} your age is {age} years old")
print(f"hello {name} your age after 5 years is {age+5} years old")

#Ask for city and favorite color
#Combine all inputs into a custom message
city=input("Enter ou favourite city:")
color=input("Enter ou favourite color:")
print(f"In {city} {color} looks beautiful")