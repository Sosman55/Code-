import random

def joue():
    user = input("'choisis' , 'p' for pierre,'f' for feuille,'c' pour ciseau : ")
    if user not in ['p','f','c']:
        return "Cette option n'existe pas veuillez choisir entre 'p','f' ou 'c'."
    computer = random.choice(['p','f','c'])
    if user==computer:
        return 'égalité'
    if a_gagné(user,computer):
        return 'tu as gagné'
    return 'tu as perdu'
def a_gagné(user, computer):
    if (user=='p' and computer=='c' ) or (user=='c' and computer=='f') or (user=='f' and computer=='p') :
        return True
    if (user=='c' and computer=='p') or (user=='f' and computer=='c') or (user=='p'and computer=='f'):
        return False
print(joue())


