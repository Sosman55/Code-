import random

def joue():
    user = input("'choisit' , 'p' for pierre,'f' for feuille,'c' pour ciseau")
    computer = random.choice(['p','f','c'])
    if user==computer:
        return 'égalité'
    if a_gagné(user,computer):
        return 'tu as gagné'
    return 'perdu'
def a_gagné(user, computer):
    if (user=='p' and computer=='c' ) or (user=='c' and computer=='f') or (user=='f' and computer=='p') :
        return True

