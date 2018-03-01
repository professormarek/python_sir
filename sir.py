#this program simulates an epidemic spreading through a population
#it implements a very simple SIR disease model

#going to need random numbers because this will be a "stochastic" simulation
#to implement the same relationships described by the differential equations
#(See slides)

import random

#next let's define our population

#suscepible
S = 999
#infectious
I = 1
#recovered / removed
R = 0

#compute the population size:
N = S +I +R

#count time
t = 0

#beta constant (recall the differential equations)
beta = 0.1 #this number is "calibrated" by observing the outcome of the model
#versus historical incidence
#this choice of beta is just a starting point

while(I > 0):
  #determine how each compartment (S I R) are changing on this time step
  
  #create a random trial to determine how many S people get infected by I people
  #on the current time step
  #for each person in S, perform a random trial to determine whether they become I
  deltaS = 0
  deltaI = 0
  deltaR = 0
  for i in range(S):
    #note the "S" term in the differential equation is handled by the iteration through "S" susceptible individuals
    if  random.random() < beta * I / float(N):
       #this S person becomes I
       deltaI = deltaI+1
       deltaS = deltaS-1
  #at the end of the time step (tick) ajust the final counts of S I and R
  S = S + deltaS
  I = I + deltaI
  t = t + 1
  #at the end of the time step or tick, print the current state
  print "Time: ", t, "S: ", S, "I: ", I, "R: ", R


