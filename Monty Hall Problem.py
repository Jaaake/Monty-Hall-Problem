from random import *
count = 0
total = 0

while count < 1000:
 
  Doors = [False, False, False] #creates doors
  
  truedoor = randrange(3)
  Doors[truedoor] = True #makes one of the doors True
  
  Choice = randrange(3) #chooses a door
  
  Eliminate = randrange(3) # eliminates a door
  while Eliminate == Choice or Eliminate == truedoor:
    Eliminate = randrange(3) #makes sure the computer can't eliminate the right door or the chosen door
  
  for door in range(0,3):
    if door != Eliminate and door != Choice:
      Switch = door #This represents the "contestant" switching from their original choice to the other unopened door
  
  if Doors[Switch] == True:
    total = total + 1
    
  count = count + 1
  
print "Simulation complete. The computer won", total,"out of", count 

  
