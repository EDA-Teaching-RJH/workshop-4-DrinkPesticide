## implement a program that prompts the user for 
## the name of a variable in camel case e.g 'preferredFirstName'
## Output that variable name in snake case e.g 'preferred_first_name'.
def main():
    camel_case = input("Please input a name for a camel variable: ")
    print(camels_to_snakes(camel_case))
def camels_to_snakes(c):
    snake_case = ""
    for x in c: 
        snake_case = (snake_case + capital_replacement(x))
    return snake_case
    ## iterate through the list.
    ## find the capitals in the camel account.
def capital_replacement(x):
    if x == x.upper(): 
        y = x.replace(x, (f"_{x.lower()}"))
        return y
    ## find the capitals in the camel account.
    else: 
        return x
    ## replace  
main()