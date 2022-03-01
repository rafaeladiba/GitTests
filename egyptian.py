def egyptian():
    x = int(input('Enter first number (x): '))
    y = int(input('Enter second number (y) : '))

    # on initialise le resultat à 0
    result = 0

    while y >= 1: 
        if y%2 != 0: 
            
            
            result = result + x
        else:
         
        
     
        x = x + x
        y = y // 2 # integer division
    return result
print(egyptian())