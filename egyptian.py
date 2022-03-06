def egyptian():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    # on initialise le resultat a 0
    result = 0

    while y > 0: 
        if y%2 != 0: 
            

            result = result + x
            y = y-1
        else:
         

         x = x + x
         y = y / 2 
    return result
print("result",egyptian())