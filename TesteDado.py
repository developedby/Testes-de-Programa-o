import random #para randomizar no randint()
import sys #bonus do nicolas para argv

def diceroller(dice):
    DiceRoll = []    #lista de resultados de cada roll do input
    DiceNumber = 0   #numero de jogadas de dado
    DiceSides = 0    #numero de faces de dado
    DiceSum = 0      #soma dos rolls 
    DiceResults = [] #resultado da soma dos rolls em forma de lista
    #Quebra em numero e lados
    dice = dice.split('d')
    DiceNumber = int(dice[0])
    DiceSides = int(dice[1])
    #Para cada numero em todas as jogadas de dado
    for number in range(DiceNumber):
        Rolls = random.randint(1, DiceSides) # Cada roll
        DiceSum += Rolls #Soma dos rolls
        DiceRoll.append(str(Rolls)) #lista de rolls
    DiceRoll = " ".join(DiceRoll) #mesma coisa
    Bonus = [str(DiceSum), DiceRoll] #Dicionario pra retornar com join de ":" entre os elementos
    return ": ".join(Bonus)

#print(diceroller("5d12 6d4 1d2 1d8 3d6 4d20 100d100")) sem o bonus do nicolas de fazer como system argument
#para todo argumento nos argumentos do sistema alem do primeiro:
for arg in sys.argv[1:]:
    print(diceroller(arg))
