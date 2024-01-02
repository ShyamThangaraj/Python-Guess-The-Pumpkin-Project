import turtle
import random
screen=turtle.Screen()
screen.addshape("output-onlinepngtools (1).png")
screen.addshape("output-onlinepngtools.png")
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
turtList=[t1,t2,t3]
winsList=[0,0,0]
#foreach loop
x=-100
for t in turtList:
  t.penup()
  t.speed(0)
  t.lt(90)
  t.shape("output-onlinepngtools (1).png")
  t.goto(x,0)
  x+=100
#ask the user who is going to win
choice=int(input("Which pumpkin will win? 1,2,3"))
def game():
  for i in range (20):
    for t in turtList:
      a=random.randint(1,6)
      if(a==5):#win
        t.shape("output-onlinepngtools (1).png")
        #find the index of that current turtle
        winIndex=turtList.index(t)
        #give that index a point
        winsList[winIndex]+=1
      else: #loss
        t.shape("output-onlinepngtools.png")

def checkUserChoice(choice):
  maxVal = max(winsList)
  print("Most wins is " + str(maxVal))
  #check if user the user made the correct choice
  winnerIndex = winsList.index(maxVal) 
  winnerIndex += 1
  print("This is turtle number #" + str(winnerIndex))
  if (choice==winnerIndex):
    print("Congrats, you picked the correct turtle!")
  else:
    print("You lose!")
game()
print(winsList)
#call the function with the parameter 
checkUserChoice(choice)


