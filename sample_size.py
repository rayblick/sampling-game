# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:01:31 2014

@author: uqrblick
"""

import random
import math
from tkinter import *

#   def the game variables!! n etc
   
class Application(Frame):
    """The guessing game: Guess N"""
    alpha=1.96
    beta=0.84
    mu1=random.randrange(20,40,1)
    sd=round(mu1*(5/30))
    loss=random.randrange(1,20,1)
    mu2= mu1-mu1*(loss/100)
    n=((alpha+beta)/((mu2-mu1)/sd))**2
   
 
    def __init__(self, master):
        """ Initialize the Frame"""        
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
    
   
    def create_widgets(self):
        """Create game buttons"""
        # first button
        self.instruction=Label(self, text="Guess N! -> If your population has a size of %s and standard deviation of %s,\n what sample size is required to find a loss of %s percent, \n (alpha = 5 percent and power = 80 percent)" %(self.mu1,self.sd,self.loss)) 
        self.instruction.grid(row=0,column=0,columnspan=2,sticky=W)
        
        self.guess=Entry(self)
        self.guess.grid(row =2,column=1,sticky=W)
        
        self.submit_button = Button(self,text="Submit",command=self.reveal)
        self.submit_button.grid(row=3,column=1,sticky=W)

        self.quit_button = Button(self, text="Quit",command=self.quit)
        self.quit_button.grid(row=4,column=1,sticky=W)
        
        self.text=Text(self,width=85,height=5,wrap = WORD) # wrap determines text wrapping, WORD wraps right side of text box
        self.text.grid(row=6,column=0,columnspan=2,sticky=W)
 
 
    def reveal(self):
        """Display message based on the guess"""
        content=self.guess.get()
      
        if int(content) < self.n:
            diff = self.n - int(content)
            message="You have underestimated the number of samples by: " + str(int(math.ceil(diff))) + " --> you would need " + str(int(math.ceil(self.n))) + " samples to detect a loss of " + str(int(math.ceil(self.loss))) + "%"      
        elif self.n == int(content):
            message="Good guess, you are correct"      
        else:
            diff1 = int(content)-self.n
            message="You have overestimated the number of samples by: " + str(int(math.ceil(diff1))) + " --> you need " + str(int(math.ceil(self.n))) + " samples to detect a loss of " + str(int(math.ceil(self.loss))) + "%"      
        
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
 
#     add a loop with two buttons - 'play again' in green and 'stop playing' in red
 
root = Tk()
root.title("Play Guess N!")
root.geometry("700x250")

app = Application(root)

root.mainloop()
       
