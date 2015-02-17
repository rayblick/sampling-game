"""
Created on Tue Feb 10 08:22:55 2015

@author: uqrblick
"""

import random
from tkinter import *
import matplotlib.pyplot as plt

# create class game with variables that can be extracted individually  
class game:
    """Create the game variables. These variables are used in the run class. """
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def playgame(self):
        """Assigns x sd and loss to variables, and calculates x2 and N which can be extracted by the user."""
        self.mu1=random.randrange(20,40,1)
        self.sd=round(self.mu1*(5/30))
        self.loss=random.randrange(5,20,1)
        self.mu2= self.mu1-self.mu1*(self.loss/100)
        self.n=((self.alpha+self.beta)/((self.mu2-self.mu1)/self.sd))**2
    
    def getPopSize(self):
        """Returns X1 to the user."""
        return self.mu1
    
    def getLoss(self):
        """Returns Loss to the user."""
        return self.loss
        
    def getSD(self):
        """Returns SD to the user."""
        return self.sd
     
    def getN(self):
        """Returns the calculate size of N to the user."""
        return self.n
    
    def setN(self, n):
        """Used to override N by the user."""
        self.n = n 

#Create the class which executes the game class
class run:
    """Run the game by getting input from the user and instantiating the game class."""
    def __init__(self):
        """Initialize empty lists to save data from each user."""
        self.estimate=[]
        self.Guess_ID=0 
        self.guess_order=[]
        self.SizeOfLoss=[]

        
    # allow user inputs to set the alpha and beta statistics
    def getInputs(self):
        """Get inputs from the user to define alpha and beta statistics"""
        try:
            self.alpha = eval(input("Enter the desired alpha statistic (5% = 1.96): "))
            self.beta = eval(input("Enter the desired beta statistic (80% = 0.84): "))
            return self.alpha, self.beta
        except:
            print('your entry must be a number')
            self.mainloop()

    # Main loop which instantiates our game class
    def mainloop(self):
        """Run the main loop which instantiates the game class and evaluates user input"""
        #global Guess_ID
        self.Guess_ID += 1
        self.guess_order.append(self.Guess_ID)
              
        alp, bet = self.getInputs()
        p1 = game(alp,bet)
        p1.playgame()
        pop=p1.getPopSize()
        los=p1.getLoss()
        self.SizeOfLoss.append(los)  
        sd=p1.getSD()
        print("\nFor a population mean of %s and sd of %s, what sample size would you use to detect a loss of %s percent" %(pop, sd, los))
        
        # I need to make this more secure (this currently fails with letters)    
        self.guessN = input("Guess %s: Enter your guess here: " %self.Guess_ID) 
        
        # assign what happens with the users input    
        if float(self.guessN) > p1.getN()+1: # provide a small margin of error + or - 1 sample (but allow rounding down to zero)
            res=round(float(self.guessN) - p1.getN())
            self.estimate.append(res)

            print("\nYou overestimated the required sample size by ", res)
    
            userEntry = input("Try again? Enter y to continue, or any key to exit: ")    
            if userEntry == 'y': # make enter work without letters... and make n active with everything else failing to execute
                p1.playgame()
                self.mainloop()

               
        elif float(self.guessN) < p1.getN()-1: # provide a small margin of error + or - 1 sample (but allow rounding down to zero)
            res= round(p1.getN() - float(self.guessN))
            self.estimate.append(-1 * res) # ensure that underestimates have a negative sign
            print ("\nYou underestimated the required sample size by ", res)
    
            userEntry = input("Try again? Enter y to continue, or any key to exit: ")        
            if userEntry == 'y':
                p1.playgame()
                self.mainloop()

        else:
            print("Your guess was correct")
            self.estimate.append(0)  
            userEntry = input("Try again? Enter y to continue, or any key to exit: ") 
            if userEntry == 'y':
                p1.playgame()
                self.mainloop()

class plot:
    """Create a histogram of the existing data stored by the user."""
    def __init__(self):
        self.histogram
    
    def histogram(self):
         # need a plotting function
        plt.hist(self.estimate,bins=15,histtype='stepfilled',color='b',alpha=0.5)
        pylab.ylim([0,len(self.estimate)*1.05])
        pyplot.title('Histogram of your guessN results')
        pyplot.xlabel('Underestimates (-) or overestimates (+) of N')
        pyplot.ylabel('Frequency')
   
# game start
p1=run()
p1.mainloop()
print("\nThese are your results. Negative values are underestimates, positive values are overestimates")
plot.histogram(p1)
