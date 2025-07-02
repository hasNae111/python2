
import math

# def horaire_sup( ):
#     nom = input("ENTRER VOTRE NOM: ")
#     salaire_horaire = float(input("ENTRER VOTRE SALAIRE: "))
#     nb_heure = float(input("Entrer le nombre d'heure que tu as travaillees:"))
#     if int(nb_heure) > 40:
#         salaire_horaire2 = float(salaire_horaire) * 1.5
#         salaire_total = salaire_horaire * 40 + salaire_horaire2 * ((nb_heure) - 40)
#
#     else:
#         salaire_total = salaire_horaire * nb_heure
#
#     print(f'Bonjours {nom}, votre salaire est {salaire_total}')
#
# horaire_sup()

#challenge2

# def somdiff(n1,n2):
#     somme= n1+n2
#     difference=n1-n2
#     return somme, difference
#
# n1= float(input("Entrer un nombre: "))
# n2 = float(input("Entrer un nombre: "))
# s,d=somdiff(n1,n2)
# print(f"la somme est {s} et la difference est {d}")

#challenge3
#question1
# n=int(input("Entrer un nombre entier"))
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# f=fact(n)
# print("le produit facctiorel de n est", f)

#question 2
# m=int(input("Entrer un nombre entier"))
# def mult(m):
#     for i in range(0,11):
#         print(f'{m}*{i}={m*i}')
# tab_mult= mult(m)
# print(f'le tableau de multiplication de {m} est: {tab_mult} ')

#question3
# l=int(input("Entrer un nombre entier"))
# def parf(l):
#     if l%math.sqrt(l)==0:
#         print("c'est un carre parfait")
#     else:
#         print("c'est un carre non parfait")
#
# p=parf(l)
# print(p)

#question4

# ch=input("Entrer une chain de charactere")
# def char(ch):
#     y=len(ch)
#     for i in range(0,y):
#         print(ch[i])
# pp=char(ch)
# print(pp)

# #question 5
# phrase=input("Entrer une phrase")
# def lgmot():
#     mots=phrase.split()
#     mmm=max(mots, key=len)
#     print('le plus long mot est:', mmm)
# lgmot()


#question6

def occ(chaine):
    calcul={}
    for i in chaine:
        calcul[i]=calcul.get(i,0)+1
    for ch, nbr in calcul.items():
            print(f'char: {ch}, le nombre d\'occurrence: {nbr}')

occ("chaine")


