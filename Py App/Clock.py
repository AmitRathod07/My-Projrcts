# Import Required Library
# importing whole module
from tkinter import *
from tkinter.ttk import *
 
# importing strftime function to
# retrieve system's time
from time import strftime
 
# creating tkinter window
root = Tk()
root.title('Clock')
 
# This function is used to
# display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
 
# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'red',
            foreground = 'black')
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()
 
mainloop()

'''

Simple animation game

# required modules
from turtle import * 
from random import randint
   
      
# classic shape turtle
speed(0)
penup()
goto(-140, 140)
   
# racing track
  
for step in range(15):
    write(step, align ='center')
    right(90)
      
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
          
    penup()
    backward(160)
    left(90)
    forward(20)
  
# first player details
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')
   
# first player proceeds to racing track
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()
   
# 360 degree turn
for turn in range(10):
    player_1.right(36)
  
# second player details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')
   
# second player enters in the racing track
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()
   
# 360 degree turn
for turn in range(72):
    player_2.left(5)
  
# third player details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')
   
# third player enters in the racing track
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()
   
# 360 degree turn
for turn in range(60):
    player_3.right(6)
  
# fourth player details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')
   
# fourth player enters in the racing track
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()
   
# 360 degree turn
for turn in range(30):
    player_4.left(12)
  
# turtles run at random speeds
for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))

'''