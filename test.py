def capital_replacement(x):
    if x == x.upper(): 
        print("True")
        y = x.replace(x, (f"_{x.lower()}")) 
        return y
    else: 
        return x
print(capital_replacement("k"))