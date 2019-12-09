import random
print("I will flip a coin 1000 times. Guess how many times it will come up heads. (Press enter to begin)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads = heads + 1
    if flips == 900:
        print("900 flips and there have been " + str(heads) + " heads.")
    if fleps == 100:
        print("At 100 flips, heads has come up " + str(heads) + " heads.")
    if flips == 500:
        print("Halfway done, and heads has come up " + str(heads) + " times.")
    flips = flips + 1


print()
print("out of 1000 coin tosses, heads came up " + str(heads) + " times!")
print("Were you close?")