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
    max_guess = int(input("Enter the maximum number of tries. "))
    max_guess -= 1
    while i:
        guess = int(input("Guess an integer from 1 to %d! (If you are continuing, it is the same number. If you won previously, it is a different number.)  " % num))
        #secret_number = random.randint(0, num)
        if max_guess == count:
            print("That was incorrect. ")
            print("Game over. You have reached the maximum number of tries, %d" % count)
            i = False
            n = False
        elif guess == secret_number:
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
            difference = abs(secret_number - guess)
            count += 1
            # if guess > secret_number:
            #     print("You guessed too high.")
            print(difference)
            print(num / 10)
            if (guess > secret_number) and (difference >= (num / 2)):
                print("You guessed too high.")
            # elif (guess > secret_number) and ((difference <= (num * 0.25)) and (difference >= (num * 0.1))):
            #     print("You guessed high.")
            elif (guess > secret_number) and (difference <= (num / 10)):
                print("You guessed a little high.")
            elif (guess > secret_number):
                print("You guessed high.")
            elif (guess < secret_number) and (difference <= (num / 10)):
                print("You guessed a little low.")
            # elif (guess < secret_number):
            #     print("You guessed low.")
            elif (guess < secret_number) and (difference >= (num / 2)):
                print("You guessed too low.")
            elif (guess < secret_number):
                print("You guessed low.")
            # else:
            #     print("You guessed too low.")
