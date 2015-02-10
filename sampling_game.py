"""
Created on Tue Feb 10 08:22:55 2015

@author: uqrblick
"""

import random
from tkinter import *

# create class game with variables that can be extracted individually  
class game:
    """The guessing game: Guess N"""
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def playgame(self):
        self.mu1=random.randrange(20,40,1)
        self.sd=round(self.mu1*(5/30))
        self.loss=random.randrange(1,20,1)
        self.mu2= self.mu1-self.mu1*(self.loss/100)
        self.n=((self.alpha+self.beta)/((self.mu2-self.mu1)/self.sd))**2
    
    def getPopSize(self):
        return self.mu1
    
    def getLoss(self):
        return self.loss
        
    def getSD(self):
        return self.sd
     
    def getN(self):
        return self.n
    
    def setN(self, n):
        self.n = n 


# allow user inputs to set the alpha and beta statistics
def getInputs():
    alpha = eval(input("Enter the desired alpha statistic (5% = 1.96): "))
    beta = eval(input("Enter the desired beta statistic (80% = 0.84): "))
    return alpha, beta

# open an empty list to record guesses
estimate=[]

# Main loop which instantiates our game class
def main():
    alp, bet = getInputs()
    p1 = game(alp,bet)
    p1.playgame()
    pop=p1.getPopSize()
    los=p1.getLoss()
    sd=p1.getSD()
    print("For a population mean of %s and sd of %s, what sample size would you use to detect a loss of %s percent" %(pop, sd, los))
    guessN = input("Enter your guess here: ") 
    
    # assign what happens with the users input    
    if float(guessN) > p1.getN():
        res=round(float(guessN) - p1.getN())
        estimate.append(res)
        print("\nYou overestimated the required sample size by ", res)
        userEntry = input("Do you want to try again? (y/n):  ")    
        if userEntry == 'y':
            p1.playgame()
            main()
            
    elif float(guessN) < p1.getN():
        res= round(p1.getN() - float(guessN))
        estimate.append(-1 * res)
        print ("\nYou underestimated the required sample size by ", res)
        userEntry = input("Do you want to try again? (y/n):  ")        
        if userEntry == 'y':
            p1.playgame()
            main()

    else:
        print("Your guess was correct")
        userEntry = input("Do you want to try again? (y/n):  ") 
        estimate.append(0)
        if userEntry == 'y':
            p1.playgame()
            main()
    
