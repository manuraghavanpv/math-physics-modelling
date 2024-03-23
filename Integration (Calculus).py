import matplotlib.pyplot as plt
import numpy as np
import math

#First Step is to set the limits
a = -2
b = 4

#Step two is to define the intervals
n = 50 #n is the number of intervals
dx = (b-a)/n #dx is the width of one interval

#Now we define some essential variables for our code
Integration = 0 #This is the variable to store our sum
i = 0 #This is our iteration variable to count the number of iterations

#The next step is to define empty lists for our code
x = [] #list for our x-values
f = [] #list for our original f(x)....(i.e., for first curve)
Nf = [] #list for our integrated f(x)....(i.e, for second curve)

#Now we go on to write the proper code
while i<n:
    midpoint = (2*a + (2*i + 1)*dx)
    x.append(midpoint)
    f.append((midpoint)**3 + 1)
    Nf.append(Integration)
    i = i + 1
print("Integrated Value:", Integration)

#Now we add the finishing touches to label the graph

#For the f(x) plot
plt.plot(x,f)
plt.xlabel("x")
plt.ylabel("f(x)/Nf(x)")

#For the Nf(x) plot
plt.plot(x, Nf)
plt.xlabel("x")
plt.ylabel("f(x)/Nf(x)")
plt.show()