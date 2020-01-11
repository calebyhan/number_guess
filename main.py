import random

# num = 1000
# secret_number = random.randint(0, num)
n = True
i = True
#count = 0

while n:
    count = 0
    # print(secret_number)
    num = int(input("Pick a number for your maximum. "))
    secret_number = random.randint(0, num)
    print(secret_number)
    i = True
    max_guess = int(input("Do you want to set a maximum amount of tries? Enter 0 if you don't want a maximum amount of guesses. "))
    if max_guess == 0:
        max_guess = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    else:
        max_guess -= 1
    while i:
        comparison = int(input("Guess an integer from 1 to %d! (If you are continuing, it is the same number. If you won previously, it is a different number.)  " % num))
        #secret_number = random.randint(0, num)
        if max_guess == count:
            print("That was incorrect. ")
            print("Game over. You have reached the maximum amount of tries. ")
            i = False
            n = False
        elif comparison == secret_number:
            count += 1
            print("You got it!")
            print("It took you", count, "tries!")
            secret_number = random.randint(0, num)
            yn = input("Do you want to try again? y/n ")
            if yn == "y":
                i = False

            elif yn == "n":
                i = False
                n = False

        else:
            count += 1
            # if comparison > secret_number:
            #     print("You guessed too high.")
            if (comparison * 1.5) > secret_number:
                print("You guessed too high.")
            elif ((comparison * 1.25) > secret_number) and ((comparison * 1.5) < secret_number):
                print("You guessed high.")
            elif ((comparison * 1.10) > secret_number) and ((comparison * 1.25) < secret_number):
                print("You guessed a little too high.")
            elif ((comparison * 0.10) < secret_number) and ((comparison * 0.25) > secret_number):
                print("You guessed a little too low.")
            elif ((comparison * 0.25) < secret_number) and ((comparison * 0.5) < secret_number):
                print("You guessed low.")
            elif (comparison * 0.5) < secret_number:
                print("You guessed too low.")
            # else:
            #     print("You guessed too low.")
