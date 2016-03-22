from random import randint
dice_number = input("Number of dice to be rolled: ")
results = []
for i in range(0, dice_number):
    x = randint(1,6)
    results.append(x)
print results
print "Total: " + str(sum(results))
