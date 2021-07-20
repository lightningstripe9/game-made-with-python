import random
print("welcome to guess the number guess numbers from 1 to 10")

number = random.choice([1, 2, 4, 5, 6, 7, 8, 9, 10])
user = int(input("enter a number: "))
while (user != number):
    user = int(input("try again: "))
if (user == number):
    print("congrats you found the correct number")