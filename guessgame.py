import random

computer_number = random.randint(10, 20)
attempts = 0

while True:
    user_number = int(input())
    attempts = attempts + 1

    if user_number == computer_number:
        print("you win!!!")
        break
    elif user_number < computer_number:
        print("go up ⬆")
    elif user_number > computer_number:
        print("go down ⬇")


print("Your attempts:", attempts, "\nEnd of Game ")
