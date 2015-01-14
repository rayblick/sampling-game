# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 15:01:31 2014

@author: uqrblick
"""


import random
import math

alpha=1.96
beta=0.84
mu1=random.randrange(20,40,1)
sd=round(mu1*(5/30))


loss=random.randrange(1,20,1)
mu2= mu1-mu1*(loss/100)
n=((alpha+beta)/((mu2-mu1)/sd))**2


print("For power=80% and alpha=0.05%")

print("The population mean is "+ str(mu1) + " and the SD is " + str(sd))
print("Guess the sample size required to detect a loss of " + str(loss)+"%")
#print(n)
guess_n= input("Guess N:")
#print("Your guess was: " + str(guess_n))
#print(mu2)

print("The calculated N was: " + str(int(math.ceil(n))))

if int(guess_n) < n:
    diff = n - int(guess_n)
    print ("You have underestimated the number of samples by: " + str(int(math.ceil(diff))))
    print ("You would need " + str(int(math.ceil(n))) + " samples to detect a loss of " + str(int(math.ceil(loss))) + "%")

elif int(guess_n) == int(math.ceil(n)):
    print ("Excellent guess, you are correct")
    print ("You need " + str(int(math.ceil(n))) + " samples to detect a loss of " + str(int(math.ceil(loss))) + "%")

else:
    diff1 = int(guess_n)-n
    print ("You have overestimated the number of samples by: " + str(int(math.ceil(diff1))))
    print ("You would need " + str(int(math.ceil(n))) + " samples to detect a loss of " + str(int(math.ceil(loss))) + "%")

