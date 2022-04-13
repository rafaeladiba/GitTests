
class syrracuseClass:
    def __init__(self,u):
        self.u=u
    
    def getNextValue(self,u):
        if self.u%2==0:   # u%2: reste de la division euclidienne de u par 2
            self.u = u//2  # u//2: quotient de la division euclidienne de u par 2
        else:
            self.u = 3*u+1
        return self.u
        

def syrracuse():
    
    u=int(input("Mettez une valeur: "))
   
    syrracuseElement = syrracuseClass(u)
    fichier = open("test.txt","a")
    fichier.truncate(0)
    #liste = []
    #liste.append(u)
    fichier.write(str(u)+" ")
    while syrracuseElement.u !=1:# tant que u different de 1
        syrracuseElement.getNextValue(syrracuseElement.u)
        string = str(syrracuseElement.u) + " " 
        fichier.write(string)
   
        

        #liste.append(syrracuseElement.u)
    fichier.close()
    #return liste
        
syrracuse()
 
 