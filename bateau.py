import random

class Bateau(object):
    "def bateau"

b1=Bateau()
b1.volume=17

print ("la capacité du bateau est de" + str(b1.volume))

liste={}

for i in range(7):
    v=random.randint(0,17)
    p=random.randint(0,5)
    o="obj"+str(i)
    liste[o]=[v,p]

print("voici un liste d'objet dont vous avez le volume et le prix auquel vous pouvez le vendre")

print (liste)

print ("sélectionner les objet pour maximiser votre bénéfice")


q=input("combien d'objet voulez-cous sélectionner?")
q=int(q)
choix=[]

for i in range(q):
    
    obj=input("sélectionner votre " +str(i)+"° object")
    choix.append("obj"+str(obj))

print (choix)
