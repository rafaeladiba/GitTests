def syrracuse():
    holaaaa
    u=int(input())
    while u!=1:# pour i allant de 1 à n
        if u%2==0:   # u%2: reste de la division euclidienne de u par 2
            u = u//2  # u//2: quotient de la division euclidienne de  u par 2
        else:
            u = 3*u+1
        print(u)
        
syrracuse()