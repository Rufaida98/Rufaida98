import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['brown','black','pink','cyan','blue','purple','green','yellow','orange','red']

def game_of_turtles():
  racers = 0
# checking that if the input is digit
  while True :
    racers = input("choose number of turtles (2 -10): ")
    
    if racers.isdigit():
      racers = int(racers)
    else:
      print("Input invalid..choose a number!!")
      continue
      
    if 2 <= racers <= 10:
      return racers
    else:
      print("Number out of range (2 - 10)..choose again!!")

def race(colors):
  turtles = create_turtles(colors)
# racing the turtles at random
  while True:
    for racers in turtles:
      distance = random.randrange(1,20)
      racers.forward(distance)

      x,y = racers.pos()
      if y>= HEIGHT//2 - 10:
        return colors[turtles.index(racers)]
      
def create_turtles(colors):
#setting the conditions for the turtles(color,shape,position,....etc)
  turtles = []
  spacingx = WIDTH // (len(colors) + 1)
  for i, color in enumerate(colors):
    racers = turtle.Turtle()
    racers.color(color)
    racers.shape('turtle')
    racers.penup()
    racers.setpos(-WIDTH // 2 +(i+ 1) * spacingx, -HEIGHT // 2 + 20)
    racers.pendown()
    racers.left(90)
    turtles.append(racers)
    
  return turtles
    
def init_turtles() :
# initializing the screen of the game
  screen = turtle.Screen()
  screen.setup (WIDTH, HEIGHT)
  screen.title("Turtle Game")
  
racers = game_of_turtles()
init_turtles()

# random shuffling of the turtles colors
random.shuffle(COLORS)
colors = COLORS[:racers]


winner = race(colors)
print("the winner is with color:", winner)
time.sleep(5)

