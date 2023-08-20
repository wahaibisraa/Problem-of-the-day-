def is_good_turn(x, y):
    return x + y > 6

x = int(input("Enter the value on Chef's dice: "))
y = int(input("Enter the value on Chefin's dice: "))

summ = x + y
print("The sum is: ", summ)

if is_good_turn(x, y):
    print("It was a good turn!")
else:
    print("It was not a good turn.")
