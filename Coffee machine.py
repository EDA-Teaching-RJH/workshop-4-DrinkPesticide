## coffee machine
## The coffee machine only accepts cash
## only 50p, 20p, 10p and 5p
## Prompt the user for an integer one at a time.
## add the integer to a variable each time,
## when the amount reaches 75p or higher inform the user and 
## return a change value = input - 75
## challenge: add extra drink and different size options
def main():
    machine_balance = 0
    print("User warning: This machine ONLY TAKES CASH;")
    print("5p, 10p, 20p and 50p coins only, NO NOTES")
    while machine_balance < 75: 
        coin_value = int(input("Please insert a coin of the right value. (Don't include 'p'): "))
        authenticate_coin(coin_value)
        machine_balance = machine_balance+coin_value
        print(machine_balance)
    change = (machine_balance - 75)
    if change > 0: 
        message = f"Your change is {change}p. Please take your coffee. Thank you!"
    elif change == 0:
        message = "No change. Please take your coffee. Thank you!"
    print(message)
## Main will prompt an input. Main will explain which 
## takes an input and adds it to a balance held in this module
## takes an input and adds it to a balance held in this module if it is 75
def authenticate_coin(c_v):
    if c_v == 5 or 10 or 20 or 50:
        print("Change correct")
        return c_v 
    if c_v != (5 or 10 or 20 or 50):
        print("Change incorrect")
        x = 1
        while x == 1:
            c_v = int(input("Coin was invalid. Insert another coin. (Don't include 'p'): "))
            print(c_v)
            if c_v == (5 or 10 or 20 or 50):
                x = x - 1
            else:
                x = x
        return c_v
main()