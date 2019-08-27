#Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

def calc_coins():
    dollarAmount = 8.69
    piggyBank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    centAmount = dollarAmount *100
    quart = int(centAmount/25)

    piggyBank["quarters"] = quart
    centAmount = (centAmount % 25)
    dimes = int(centAmount/10)

    piggyBank["dimes"] = dimes
    centAmount = (centAmount % 10)
    nicks = int(centAmount/5)

    piggyBank["nickels"] = nicks
    centAmount = (centAmount % 5)
    pens = int(centAmount)

    piggyBank["pennies"] = pens

    print(piggyBank)







calc_coins()

