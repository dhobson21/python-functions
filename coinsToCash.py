#Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.
#For each coin type, give yourself as many as you like.
#Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.


def calc_dollars():
    piggy_bank = dict()
    piggy_bank = {
        "pennies": 252,
        "nickels": 75,
        "dimes": 60,
        "quarters": 45
    }
    dollar_amount = (piggy_bank["pennies"] * 1 + piggy_bank["nickels"] *5 + piggy_bank["dimes"] *10 + piggy_bank["quarters"] * 25) / 100

    print(f'${dollar_amount}')

calc_dollars()