#Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

def print_numbers():
    for i in range(100):
        #For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
        if (i+1) % 5 is 0 and (i+1) % 7 is 0:
            print("ChickenMonkey")
        elif (i+1) % 5 is 0:
            print("Chicken")
        elif (i+1) % 7 is 0:
            print("Monkey")
        else:
            print(i+1)

print_numbers()

