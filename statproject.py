import random
import numpy as np
import matplotlib.pyplot as plt

figure, axis = plt.subplots(2, 2) 

def flipCoin(numFlips):
    numheads = 0
    for i in range(numFlips):
        numheads += random.randint(0,1)
    return numheads
    

def rollDie(numRolls):
    numheads = 0
    for i in range(numRolls):
        numheads += random.randint(1,6)
    return numheads


def coinHistogram(numTrials,numFlips,x,y):
    trials = []
    for i in range(numFlips):
        trials.append(rollDie(numFlips))
    axis[x,y].hist(trials)
    axis[x,y].set_title("Trials: " + str(numFlips))

def diceHistogram(numTrials,numRolls,x,y):
    trials = []
    for i in range(numTrials):
        trials.append(rollDie(numRolls))
    axis[x,y].hist(trials)
    axis[x,y].set_title("Trials: " + str(numRolls))
    


diceHistogram(1000,10,0,0)
diceHistogram(1000,20,1,0)
diceHistogram(1000,40,0,1)
diceHistogram(1000,80,1,1)

plt.tight_layout() 
plt.show()