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
    while i:
        comparison = int(input("Guess an integer from 1 to %d! (If you are continuing, it is the same number. If you won previously, it is a different number.)  " % num))
        #secret_number = random.randint(0, num)

        if comparison == secret_number:
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
            if comparison > secret_number:
                  print("You guessed too high.")
            else:
                  print("You guessed too low.")
