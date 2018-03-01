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

#beta constant (recall the differential equations) - affects infection rate
beta = 0.1 #this number is "calibrated" by observing the outcome of the model
#versus historical incidence
#this choice of beta is just a starting point

#gamma constant - affects recovery rate
gamma = 0.05 #initial value - needs to be calibrated

while(I > 0):
  #determine how each compartment (S I R) are changing on this time step
  
  #create a random trial to determine how many S people get infected by I people
  #on the current time step
  #for each person in S, perform a random trial to determine whether they become I
  deltaS = 0
  deltaI = 0
  deltaR = 0
  #model the change in Susceptible and Infectious - proportionate to both S and I
  for s in range(S):
    #note the "S" term in the differential equation is handled by the iteration through "S" susceptible individuals
    if  random.random() < beta * I / float(N):
       #this S person becomes I
       deltaI = deltaI+1
       deltaS = deltaS-1
  #model change in Infectious individuals becoming R - proportionate to the current number of I and gamma
  for i in range(I):
    if random.random() < gamma:
      deltaI = deltaI - 1
      deltaR = deltaR + 1
  #at the end of the time step (tick) adjust the final counts of S I and R
  S = S + deltaS
  I = I + deltaI
  R = R + deltaR
  #update time
  t = t + 1
  #at the end of the time step or tick, print the current state
  print "Time: ", t, "S: ", S, "I: ", I, "R: ", R

#TODO: exercise, create an animated plot (updates every tick)
#don't forget to pause for a moment between ticks so that the user can see what is happening!

