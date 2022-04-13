def syrracuse():
    
    u=int(input("Mettez une valeur: "))
    liste = []
    liste.append(u)
    while u!=1:# tant que u different de 1
        if u%2==0:   # u%2: reste de la division euclidienne de u par 2
            u = u//2  # u//2: quotient de la division euclidienne de  u par 2
        else:
            u = 3*u+1
        liste.append(u)
    return liste
        
print(syrracuse())