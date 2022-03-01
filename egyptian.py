def egyptian():
    x = int(input('Enter first number (x): '))
    y = int(input('Enter second number (y) : '))

    # on initialise le resultat à 0
    result = 0

    while y >= 1: 
        if y%2 != 0: 
            print('x =', x, 'and', 'y =', y)
            print('  ADD', x)
            result = result + x
        else:
         print('x =', x, 'and', 'y =', y)
        
     
        x = x * 2
        y = y // 2 # integer division