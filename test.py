def capital_replacement(x):
    if x == x.upper: 
        y = x.replace(x, ('_' + x.lower))
        return y
print(capital_replacement("K"))