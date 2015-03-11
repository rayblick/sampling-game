#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 13:24:25 2015
Last modified on Wednesday Mar 11 19:02:00 2015
@author: uqrblick
"""
from tkinter import *
from tkinter import ttk
import random, math
import matplotlib
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class guessN:

    def __init__(self, master):
        self.Guess_ID = 0
        self.error_data = [0,1]
        self.guess = []
        self.calculated_N = []
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        master.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure('TLabel', font = ('Arial',11))
        self.style.configure('Header.TLabel',font = ('Arial', 20, 'bold'))
      
        # build the application header
        self.img = PhotoImage(file = "images//nlogo.gif").subsample(5, 5)
        ttk.Label(self.frame_header, image = self.img, anchor = CENTER).grid(row = 0, column = 0, rowspan = 2, padx = 10, pady = 10)
        ttk.Label(self.frame_header, text = "Welcome to guessN!", style='Header.TLabel').grid(row = 0,column = 1, padx = 10, pady = 10)
        ttk.Label(self.frame_header, wraplength = 640, text = ("Evaluate your own skill in guessing how many samples " 
                                                    "you need to record a loss in a population...\n")).grid(row = 1, column = 1, padx = 10)      
       
        # create a frame to hold the content
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack(side = LEFT)
        
        # assign a label to the user entry field
        ttk.Label(self.frame_content,text = "Enter your guess below...").grid(row = 1, column = 0)
    
        # assign entry field associated with the users guess
        self.entry_guessN = ttk.Entry(self.frame_content, width = 24)
        self.entry_guessN.bind("<Return>", (lambda e: self.submit()))
        
        self.text_instructions = Text(self.frame_content, width = 65, height = 4, font = ('Arial', 11))
        self.text_results = Text(self.frame_content, width = 65, height = 4, font = ('Arial', 11))
        
        # specify the location of widgets
        self.entry_guessN.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.text_instructions.grid(row = 0, column = 0, columnspan = 3,padx = 10, pady = 10)
        self.text_results.grid(row = 4, column = 0, columnspan = 3, padx = 10, pady = 15)

        
        # Add buttons for playing and quiting the program
        self.PlayButton =  ttk.Button(self.frame_content, text = "Play", underline = 0, command = self.play)
        self.PlayButton.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.SubmitButton = ttk.Button(self.frame_content, text = "Submit", underline = 0, command = self.submit, state = DISABLED)
        self.SubmitButton.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.ClearButton = ttk.Button(self.frame_content, text = "Clear", underline = 0, command = self.clear)
        self.ClearButton.grid(row = 2, column = 2, padx = 5,pady = 5)
        self.ExitButton = ttk.Button(self.frame_content, text="Exit game", underline = 0, command= self.exit_game)
        self.ExitButton.grid(row = 3, column = 2, padx = 5, pady = 5)

        # bind quick keys
        root.bind("<Control-p>", (lambda e: self.play()))
        root.bind("<Control-s>", (lambda e: self.submit()))
        root.bind("<Control-c>", (lambda e: self.clear()))
        root.bind("<Control-e>", (lambda e: self.exit_game()))

        
        # Create plotting frame
        self.frame_plot = ttk.Frame(master)
        self.frame_plot.pack(side = RIGHT)

        # Add a canvas for plotting
        self.f = Figure(figsize=(6,6), dpi = 50)
        self.a = self.f.add_subplot(1, 1, 1)
        self.a.hist(self.error_data, bins = 15)

        self.canvas = FigureCanvasTkAgg(self.f, master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack()
        self.canvas._tkcanvas.pack(padx = 15, pady = 10)     


    def play(self):
        """Assigns a mean population size (mu) sd and the percentage of loss to game variables, 
        and calculates the new mean (after loss) and the required N to realiably detect the loss."""

        self.mu1 = random.randrange(20, 40, 1)
        self.sd = round(self.mu1 * (5 / 30))
        self.loss = random.randrange(5, 20, 1)
        self.alpha = 1.96 # set to 5%
        self.beta = 0.84 # set to 80%
        self.mu2 = self.mu1 - self.mu1 * (self.loss / 100)
        self.n = ((self.alpha + self.beta) / ((self.mu2 - self.mu1) / self.sd))**2

        # clear all fields        
        self.clear()
        
        # Add instruction text to the first text window
        self.instruction_message = ("If you have a sample mean of %s and a standard deviation of %s,"
                                    "\nwhat sample size is required to detect a loss of %s percent? \n"
                                    "\nNote: alpha = 5 percent and power = 80 percent" %(self.mu1, self.sd, self.loss))
        
        self.text_instructions.insert(0.0, self.instruction_message)
        #
        # change button states to guide the player
        self.PlayButton.state(["disabled"])
        self.SubmitButton.state(["!disabled"])
        self.entry_guessN.state(["!disabled"])
      
    def submit(self):
        """        
        The submit function takes the information from the users entry,
        and compares it with the correct and calculated N required to detect the loss.
        This function determines three outcomes as an overestimate, underestimate or a correct guess."
        
        """ 
        content = self.entry_guessN.get()

        try:
           
            type(content) == type(int) or type(float)

            
            # if statements are adjusted to be within 1 sampling unit of the correct answer
            if int(content) <= (self.n - 1):
                diff = self.n - int(content)
                self.error_data.append(int(content) - self.n)
                self.Guess_ID += 1
                #self.guess.append(content)
                #self.calculated_N.append(self.n)
                message = "Guess # " + str(self.Guess_ID) + ": " + "You have underestimated the number of samples by " + str(int(math.ceil(diff))) + "\nYou would need " + str(int(math.ceil(self.n))) + " samples to detect a loss of " + str(int(math.ceil(self.loss))) + "%"      
               
            elif int(content) >= (self.n + 1):
                diff = int(content) - (self.n)
                self.error_data.append(int(content) - self.n)
                self.Guess_ID += 1
                #self.guess.append(content)
                #self.calculated_N.append(self.n)
                message = "Guess # " + str(self.Guess_ID) + ": " + "You have overestimated the number of samples by " + str(int(math.ceil(diff))) + "\nYou need " + str(int(math.ceil(self.n))) + " samples to detect a loss of " + str(int(math.ceil(self.loss))) + "%" 
                
            else: 
                diff = 0.0
                self.Guess_ID += 1
                self.error_data.append(0)
                #self.guess.append(content)
                #self.calculated_N.append(self.n)
                message = "Correct"

            # append the data for plotting
            self.f.clear()
            self.a = self.f.add_subplot(1, 1, 1)
            self.a.hist(self.error_data, bins = 15, color = "cornflowerblue")
            self.canvas.show()
        

            # provide message    
            self.text_results.delete(1.0, 'end')
            self.text_results.insert(0.0, message)

            # change button states to guide the player
            self.entry_guessN.delete(0, END)
            self.SubmitButton.state(["disabled"])
            self.PlayButton.state(["!disabled"])
            self.entry_guessN.state(["disabled"])
             
        except:
            self.text_results.delete(1.0, 'end')
            self.exception_message = 'Opps! Something went wrong. Try entering an integer \nor floating point number'
            self.text_results.insert(0.0, self.exception_message)
    
            
    def clear(self):
        """
        The clear function removes all entries from the fields
        """
        
        # clear entry text field
        self.entry_guessN.delete(0, END)
        
        self.text_instructions.delete(1.0, 'end')
        self.text_results.delete(1.0, 'end')

        # change button states to guide the player
        self.SubmitButton.state(["disabled"])
        self.PlayButton.state(["!disabled"])

        
    def exit_game(self):
        """
        Exit the game.
        """        
        root.destroy()        
  
root = Tk()
app = guessN(root)
root.title("guessN! (GUI) v0.2 by RayBlick")
root.mainloop()
